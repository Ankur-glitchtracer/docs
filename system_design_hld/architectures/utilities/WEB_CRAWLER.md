# 🕷️ System Design: Web Crawler & Search Indexer

## 📝 Overview
A web crawler is an automated distributed system that systematically browses the World Wide Web to extract content, generate reverse indexes, and build titles/snippets for search engines, as well as extract text data to train Large Language Models (LLMs). The core challenge is managing a massive, infinite state machine without getting trapped in cyclical loops, while serving high-volume, low-latency search queries and strictly respecting the bandwidth of target web servers.

!!! abstract "Core Concepts"
    - **Breadth-First Search (BFS) & Politeness:** Traversing the web graph while mathematically guaranteeing the crawler won't launch a DoS attack on a target web server.
    - **Pipelining & Fault Tolerance:** Breaking the crawler into separate fetch and extraction stages using message queues to isolate failures and resume seamlessly without losing progress.
    - **Reverse Indexing:** Mapping individual words/search terms back to the documents (URLs) that contain them to enable lightning-fast search queries.
    - **Content Signatures & Deduplication:** Generating signatures using algorithms like Jaccard index or Cosine similarity to detect and deduplicate similar HTML content and avoid redundant work.
    - **Crawler Traps:** Utilizing depth limiters to prevent the crawler from getting stuck in infinite auto-generated link loops.
    - **Connection Pooling & DNS Caching:** Keeping multiple open connections and locally caching IP addresses to prevent network I/O from bottlenecking the fetcher threads.

---

## 🏭 The Scenario & Requirements

### 😡 The Problem (The Villain)
The internet is essentially infinite and a messy, unpredictable place. If a crawler aggressively follows every link it sees using a naive approach, it can easily fall into "spider traps" (infinite cyclical directories) or accidentally execute a Distributed Denial of Service (DDoS) attack against external websites by ignoring crawl delays. Furthermore, when machines inevitably fail, massive bottlenecks due to DNS resolution times occur, and lost progress on a massive crawl is costly. Once data is fetched, searching across billions of unstructured HTML documents in real-time is impossible without highly optimized indexing.

### 🦸 The Solution (The Hero)
A highly concurrent, pipelined architecture centered around a prioritized "URL Frontier" that strictly governs pacing. It utilizes message queues with visibility timeouts, distributed blob storage, and centralized rate-limiting. It seamlessly pipes fetched pages into asynchronous queues to build a Reverse Index, a Document Store (for static titles and snippets), and raw text storage for LLMs. When a user searches, a dedicated Query API normalizes the input and scatter-gathers the results from the indexed clusters.

### 📜 Requirements
- **Functional Requirements:**
    1. The system must fetch web pages starting from a list of prioritized seed URLs.
    2. It must extract text content and outbound links from the HTML, storing the text for later LLM processing.
    3. It must generate a reverse index of words to pages.
    4. It must generate and store static titles and snippets for pages.
    5. Users can input a search term and see a list of relevant pages.
- **Non-Functional Requirements:**
    1. **Politeness & Cycle Prevention:** The crawler must adhere to `robots.txt` and never overwhelm a server or get stuck in an infinite loop.
    2. **Fault Tolerance:** Handle failures gracefully and resume crawling without losing progress.
    3. **High Availability & Speed:** The search generation must be fast, and the service must be highly available.
    4. **Efficiency & Scalability:** Crawl the web rapidly (e.g., 10B pages in under 5 days) and ensure freshness based on update frequency.

!!! info "Capacity Estimation (Back-of-the-envelope)"
    - **Search Engine Indexing Target:** 1 Billion target links, crawled approx. once per week $\rightarrow$ **4 Billion links crawled per month**.
    - **Search Engine Throughput:** 4 Billion / 2.5M seconds = **~1,600 write requests/sec**.
    - **Search Traffic:** 100 Billion searches per month $\rightarrow$ **~40,000 search requests/sec**.
    - **LLM Crawl Spike (Scale Target):** 10 billion pages to be crawled within 5 days.
    - **Storage (Content):** Assuming an average size of 2MB per page (including HTML/inline resources for bandwidth limits) or 500 KB average stored text. 500 KB * 4 Billion pages = **2 PB of new/updated content per month**.
    - **Total Storage:** Over 3 years, this scales to **~72 PB** of stored page content.

---

## 📊 API Design & Data Model

=== "REST APIs"
    - **`GET /api/v1/search`** *(Public Search Endpoint)*
        - **Query Params:** `?query=hello+world`
        - **Response:** ```json
        [
          {
            "title": "foo's title",
            "snippet": "foo's snippet",
            "link": "[https://foo.com](https://foo.com)"
          }
        ]
        ```

=== "Database Schema"
    - **NoSQL / KV Store:** `links_to_crawl` (Redis Sorted Sets / SQS Frontier)
        - `url` (String, PK)
        - `priority` (Float) - Determines crawl order
        - `depth` (Integer) - Tracks link hops from seed to prevent crawler traps
    - **Metadata DB:** `crawled_links` & Domain State (Cassandra / DynamoDB)
        - `url_hash` (String, PK)
        - `signature` (String) - Content hash/signature
        - `last_crawled_at` (Timestamp)
        - `domain` (String) - Mapped to `robots_txt_rules` and rate-limiting states
    - **Blob Storage:** (S3 / GFS)
        - `html_blob_link`: Pointer to raw HTML in S3.
        - `text_blob_link`: Pointer to extracted text data in S3.
    - **Search Databases:** (Lucene / Elasticsearch)
        - `Reverse Index Store:` Maps `word` $\rightarrow$ `List<url>`
        - `Document Store:` Maps `url` $\rightarrow$ `{title, snippet}`

---

## 🏗️ High-Level Architecture

### Architecture Diagram
```mermaid
graph TD
    Client[Client App] -->|Search Request| WebServer[Web Server / Query API]
    WebServer --> MemCache[(Search Memory Cache)]
    WebServer --> RevIndexSvc[Reverse Index Service]
    WebServer --> DocSvc[Document Service]
    
    Seed[(Frontier Queue / SQS)] -->|URL| Fetcher[https://fetcher.ai/](https://fetcher.ai/)
    Fetcher -->|Resolve IP| DNS[DNS Resolver Cache]
    Fetcher -->|Download HTML| Web[External Web Servers]
    Fetcher -->|Store Raw HTML| S3Raw[(S3 Raw HTML)]
    
    Fetcher -->|Raw Page Data| AsyncQueues[Message Queues / Parser Queue]
    AsyncQueues --> Extractor[Text & URL Extractor Workers]
    AsyncQueues --> RevIndexSvc
    AsyncQueues --> DocSvc
    
    Extractor -->|Read Raw HTML| S3Raw
    Extractor -->|Store Text| S3Text[(S3 Text Data)]
    Extractor -->|New Links| MapReduce[MapReduce URL Deduplicator]
    MapReduce --> Seed
    
    Fetcher -.->|Check/Update| CrawledDB[(Metadata DB)]
    Extractor -.->|Update| CrawledDB
```

### Component Walkthrough

1.  **Crawler Service (Fetcher):** Pulls the highest priority URL from the `links_to_crawl` NoSQL store / SQS Frontier. It resolves the IP via the DNS cache, checks for crawl permissions, and fetches the page. S3 is used to store the raw HTML since queues are not optimized for large payloads.
2.  **Text & URL Extractor Workers:** A separate worker stage that reads the fetched HTML from S3, extracts the desired text for LLMs, generates a signature, and extracts newly linked URLs to feed back into the Frontier.
3.  **Reverse Index Service:** Consumes from the queue, tokenizes the text, and maps individual words back to the URL.
4.  **Document Service:** Consumes from the queue to generate and store the static HTML title and short text snippet for the search results page.
5.  **Query API:** When a user searches, this server parses the query (removes markup, fixes typos, normalizes capitalization, handles boolean ops), hits the Reverse Index to rank matching documents, and uses the Document Service to hydrate the titles/snippets.

-----

## 🔬 Deep Dive & Scalability

### 🛡️ Fault Tolerance & Pipelining
Fetching web pages is the most likely task to fail, as external servers might be down or connections may timeout. If our crawler handled everything sequentially in a single monolith, a parsing failure could cause us to lose the expensive downloaded HTML. 
To handle this, we break the system into pipelined stages: the **URL Fetcher** and the **Text & URL Extractor**. If a crawler goes down mid-fetch, SQS's visibility timeout expires, making the URL visible again for another worker to pick up. Once the fetcher safely stores the HTML in S3, it deletes the message and queues a parsing job. This ensures no data is lost and allows us to scale fetching and parsing independently.

### 🤝 Politeness & Rate Limiting
We must respect a website's `robots.txt` file, checking the `Disallow` directive and the `Crawl-delay` directive to wait a specified number of seconds between requests. 
To implement this:
- We parse and store the `robots.txt` rules in our Metadata DB.
- We track the `last_crawl_time` for each domain.
- If we pull a URL from the queue but the crawl delay hasn't passed, we use SQS's `ChangeMessageVisibility` API to extend the timeout and defer processing the message for later.
- To prevent multiple concurrent crawlers from hitting the same domain simultaneously and overriding the `last_crawl_time`, we use an atomic operation like a Redis `SET NX` to acquire a per-domain lock before crawling.
- We introduce **jitter** (a small random delay) to the rate-limiting algorithm to prevent synchronized behavior where multiple crawlers wait and retry at the exact same millisecond.

### 🚀 Scaling to 10 Billion Pages in 5 Days
Web crawling is a heavily I/O-bound task. An AWS network-optimized instance (e.g., 200 Gbps) handling 2MB pages can theoretically process 12,500 pages/second. Assuming we only safely utilize 30% of this bandwidth due to practical limits, one machine achieves roughly 3,750 pages/second. 
To crawl 10 billion pages at 3,750 pages/second takes about 30.9 days on a single machine. Since this scales linearly, deploying 8 of these high-powered machines reduces the time to ~3.9 days, comfortably beating our 5-day requirement.

### 🌐 Overcoming the DNS Bottleneck
DNS resolution is a massive, frequently overlooked bottleneck, historically accounting for up to 70% of a crawler thread's elapsed time. At thousands of requests per second, making a full DNS hierarchy round-trip for every URL will cripple the system.
To optimize this, we implement **DNS caching** within our crawler nodes to reuse lookups for the same domain. Additionally, we use **multiple DNS providers** and round-robin requests between them to distribute the massive load and avoid hitting rate limits on any single provider. Connection pooling is also used to maintain open, reusable connections.

### 🔄 Deduplication & Crawler Traps
To maximize efficiency, we must not crawl the same content twice.
- **URL-Level Deduplication (MapReduce):** Before adding a URL to the frontier, we check the Metadata DB. For billions of initial links, a MapReduce job that yields `(url, 1)` only reduces/keeps URLs with a frequency of `1`.
- **Content-Level Deduplication (Signatures):** Different URLs often serve identical content. The crawler uses algorithms like the **Jaccard index** or **Cosine similarity** to generate a page signature. If it matches, we skip the expensive parsing step and heavily reduce the domain's priority to avoid cyclical traps.
- **Crawler Traps:** Sites with infinite auto-generated link loops can trap our crawlers forever. We add a `depth` field to our Metadata DB (seed URL is depth 0). If a link's depth exceeds a threshold (e.g., 15-20 hops), we immediately stop crawling that branch.

### Search Scalability
With 40,000 search requests per second, the search cluster will melt without aggressive scaling:
- **Query Caching:** Because search traffic is not evenly distributed, a Memory Cache handles the bulk of the repetitive read load. Reading 1 MB sequentially from RAM takes ~250 microseconds, 80x faster than disk.
- **Sharding & Federation:** The Reverse Index Service and Document Service must make heavy use of sharding (e.g., partitioning the index by alphabet/terms) to handle the massive data size and request load.

### ⚖️ Trade-offs

| Decision | Pros | Cons / Limitations |
| :--- | :--- | :--- |
| **SQL vs NoSQL** | SQL offers strict ACID properties. | NoSQL (Key-Value/Wide-Column) scales horizontally much better for massive write volumes and petabyte datasets. |
| **TCP vs UDP for Crawler** | TCP guarantees packet delivery and is standard for HTTP. | Switching custom fetchers to UDP could technically boost performance but sacrifices reliability and standard web compatibility. |

---

## 🎤 Interview Toolkit

- **Mid-Level Expectations:** Should be able to define the high-level data flow and implement a simple system utilizing a queue to crawl the web. Expected to discuss basic politeness (`robots.txt`) and handle simple deduplication.
- **Senior Expectations:** Must speed through the high-level design and articulate deep architectural trade-offs. Expected to understand the specifics of queue visibility timeouts for fault tolerance, deeply handle domain rate-limiting with distributed locks, and crunch the network bandwidth numbers to hit the 5-day goal. 
- **Staff+ Expectations:** Expected to proactively identify non-obvious bottlenecks, such as DNS resolution latency and content-level deduplication. Will drive the deep dives independently, discussing practical applications like adding jitter to prevent synchronized crawler thundering herds.
- **Scale Question:** "Your fetcher threads are mostly sitting idle, CPU is at 10%, but throughput is terrible. What's the bottleneck?" -> *DNS Resolution and Connection Setup. Ensure the workers are using a localized DNS cache and Connection Pooling to avoid being blocked on continuous network I/O.*
- **Failure Probe:** "How do you handle 'Spider Traps' (infinite cyclical directories)?" -> *Rely on the page signature (Cosine similarity) and strict URL depth limiters. Even if the URL structure changes dynamically, the actual text content signature will be flagged as highly similar to previously crawled pages.*
- **Edge Case (Dynamic Content):** *How do you handle Single Page Applications (SPAs) that render via JavaScript?* -> *The basic HTML fetch won't work. We would need to integrate a headless browser like Puppeteer to fully execute the JavaScript and render the DOM before extracting the text.*
- **Edge Case (Large Files):** *How do we avoid downloading 5GB PDFs?* -> *Issue an HTTP `HEAD` request first to check the `Content-Length` header. If it exceeds a safe threshold (like 10MB), skip downloading the full body.*
- **Edge Case:** "How do you ensure search queries with typos still return results?" -> *The Query API must implement a robust text normalization pipeline before hitting the Reverse Index. This includes breaking text into terms, stripping markup, stemming words, and applying typo-correction algorithms (like Levenshtein distance matching).*

## 🔗 Related Architectures
- [Architecture Patterns: MapReduce](../../pillars/ARCHITECTURE_PATTERNS.md) — Deep dive into offline URL deduplication and hit counting.
- [System Design: Twitter Search](../search_systems/TWITTER_SEARCH.md) — Excellent parallel for understanding how early-stage reverse indexing works on text streams.
- [Ad Click Aggregator](./AD_CLICK_AGGREGATOR.md) — Shares similar requirements around extremely high-volume, pipelined data ingestion and the necessity for robust fault tolerance using queues and stream processors.
