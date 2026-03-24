# 🔗 System Design: URL Shortener & Pastebin (Bitly / Pastebin)

## 📝 Overview
A distributed URL shortener or pastebin service creates short, unique aliases for long URLs or blocks of text. The system is characterized by an extreme read-heavy workload and must provide highly available, sub-millisecond redirections or text retrievals while preventing alias collisions at massive scale.

!!! abstract "Core Concepts"
    - **Base62 Encoding:** Converting hashes or numerical IDs into a short string of 62 alphanumeric characters (A-Z, a-z, 0-9) to create the shortest possible, URL-safe alias.
    - **Key Generation vs. Hash Encoding:** Choosing between pre-generating keys (KGS), using distributed counters, or hashing user data (MD5) on the fly to prevent database write collisions.
    - **Offline Analytics (MapReduce):** Processing massive web server access logs asynchronously to generate read/hit statistics without impacting the critical read path.
    - **Read-Heavy Caching:** Aggressively caching popular URL mappings using LRU (Least Recently Used) eviction to protect the primary database from viral traffic spikes.

---

## 🏭 The Scenario & Requirements

### 😡 The Problem (The Villain)
Standard URLs are often hundreds of characters long, breaking easily when copy-pasted and consuming too many characters for SMS limits. Similarly, sharing large blocks of code or text in chat applications is messy. Furthermore, generating millions of unique, random 7-character strings on the fly for every user request leads to expensive database collision checks, severe write latency, and storage bloat from stale, expired links. High traffic spikes can easily cause database bottlenecks.

### 🦸 The Solution (The Hero)
A highly available service that maps short, 7-character Base62 aliases to long URLs or object storage paths (for text files). By relying on an efficient ID generation strategy and aggressive cache-first read paths, the system guarantees low-latency reads. Asynchronous worker processes handle the heavy lifting: tracking analytics via MapReduce and routinely purging expired links from the database.

### 📜 Requirements
- **Functional Requirements:**
    1. Users can submit a long URL or a block of text and receive a randomly generated short link.
    2. Clicking the short link instantly redirects to the original URL or displays the text.
    3. Users can optionally set a timed expiration (default is no expiration) and custom aliases.
    4. Service tracks monthly page view analytics.
    5. Service deletes expired links/pastes.
- **Non-Functional Requirements:**
    1. **High Availability:** The redirection service must never go down (99.99% uptime).
    2. **Low Latency:** Redirection/Reads must happen fast (reading from memory takes ~250 microseconds vs. disk taking 80x longer; overall <100ms).
    3. **Analytics:** Page view stats do not need to be real-time.
    4. **Scalability:** Must scale to support 1 billion+ shortened URLs.

!!! info "Capacity Estimation (Back-of-the-envelope)"
    - **Traffic / Ratio:** Read-Heavy system, typically a **1000:1** Read:Write ratio for URL shorteners (or 10:1 for Pastebin).
    - **Throughput:** ~6K reads/sec average $\rightarrow$ 600K reads/sec peak. Writes are ~1/sec average.
    - **Storage Size:** 1 KB text + 7 bytes `shortlink` + 4 bytes `expiration` + 5 bytes `created_at` + 255 bytes `paste_path` = **~1.27 KB per record**.
    - **Storage Total:** ~1 billion records over a few years $\rightarrow$ **~1.2 TB of storage**.
    - **Alias Capacity:** A 7-character Base62 string provides $62^7$ (~3.5 trillion) combinations, vastly exceeding the required scale.

---

## 📊 API Design & Data Model

=== "REST APIs"
    - **`POST /api/v1/urls`** (or `/paste`)
        - **Request:**
          ```json
          {
            "long_url": "[https://example.com/very/long/path](https://example.com/very/long/path)",
            "custom_alias": "my-promo",
            "expiration_length_in_minutes": 60,
            "paste_contents": "Optional text block"
          }
          ```
        - **Response:**
          ```json
          {
            "short_url": "[https://sho.rt/xyz123a](https://sho.rt/xyz123a)"
          }
          ```
    - **`GET /{alias}`**
        - **Response:** `302 Found` (Redirect to `long_url`). Returns `410 Gone` if expired.
    - **`GET /api/v1/paste?shortlink=xyz123a`**
        - **Response:**
          ```json
          {
            "paste_contents": "Hello World",
            "created_at": "YYYY-MM-DD...",
            "expiration_length_in_minutes": 60
          }
          ```

=== "Database Schema"
    - **Table:** `urls` / `pastes` (SQL or NoSQL KV Store)
        - `short_code` (Char(7), PK) - Indexed for uniqueness
        - `long_url` (Varchar) - For standard URL shortening
        - `custom_alias` (Varchar, Optional)
        - `expiration_date` (Timestamp)
        - `created_at` (Datetime) - Indexed to speed up lookups and cleanup
        - `paste_path` (Varchar 255) - Path to S3 object (if text paste)
    - **Table:** `unused_keys` (RDBMS or Key-Value for KGS approach)
        - `hash` (String, PK)
        - `is_used` (Boolean)
    - **Object Store:** (e.g., Amazon S3)
        - Stores the actual 1KB+ text content for Pastebin use cases.
    - **Analytics Database:** (Amazon Redshift / Google BigQuery)
        - Stores aggregated hit counts by year/month and URL.

---

## 🏗️ High-Level Architecture

### Architecture Diagram
```mermaid
graph TD
    Client -->|1. Create / 2. Read| LB[Load Balancer]
    
    LB --> WebServers[Web Servers / Reverse Proxy]
    
    WebServers --> ReadService[Read API]
    WebServers --> WriteService[Write API]
    
    ReadService --> Cache[(Memory Cache)]
    Cache -.->|Cache Miss| DB[(SQL/NoSQL Database)]
    ReadService --> S3[(Object Store)]
    
    WriteService --> DB
    WriteService --> S3
    WriteService -.-> KGS[Redis Counter / Key Generation Svc]
    
    LogFiles[Web Server Logs] --> MapReduce[MapReduce Analytics Worker]
    MapReduce --> AnalyticsDB[(Data Warehouse)]
    
    CleanupWorker[Cleanup Cron Job] --> DB
```

### Component Walkthrough

1. **Load Balancer:** Routes read vs write traffic across stateless application servers.
2. **Web Servers (Read/Write APIs):** Act as a reverse proxy forwarding requests to specific services.
3. **Primary Database & Cache:** The DB stores the durable mappings of short codes to destinations. A Memory Cache (Redis/Memcached) sits in front to handle the 600K+ reads/sec spikes, ensuring sub-millisecond lookups.
4. **Key Generator (Redis/KGS):** Generates unique, incrementing IDs or fetches pre-computed strings to hand off to the Write Service without DB collision checks.
5. **Object Store (S3):** Comfortably handles text payload storage, keeping the primary database lean.
6. **MapReduce Analytics:** A background process that parses access logs, extracts the year/month and URL, and aggregates hit counts into a Data Warehouse.
7. **Cleanup Worker:** An asynchronous cron job that purges expired links to free up space.

---

## 🔬 Deep Dive & Scalability

### 1. Generating Unique Short Codes
To avoid write collisions when generating the 7-character string, we evaluate three primary approaches:

- **Counter Batching + Base62 (Preferred):** Utilize an atomic, incrementing counter via a single-threaded Redis instance (`INCR`). The numeric counter is then encoded into Base62. To avoid network round-trips to Redis for every single URL creation, application servers request a batch of IDs (e.g., 1,000 at a time) to keep in local RAM.
    - *Pros:* Zero collisions, blazing fast $\mathcal{O}(1)$ allocation.
    - *Cons:* Predictable IDs allow scraping. (Fix: Apply a reversible XOR or cipher before Base62 encoding).
- **Key Generation Service (KGS):** A background daemon pre-computes millions of random 6-7 character Base62 strings offline, storing them in an `unused_keys` database. App servers load batches of these keys into RAM.
    - *Pros:* Zero collisions, completely random unpredictable keys.
    - *Cons:* Introduces extra system complexity; keys can be lost if an App Server crashes.
- **On-the-fly Hashing (MD5 + Base62):** Take the MD5 hash of the long URL (or IP + timestamp), Base62 encode it, and take the first 7 characters.
    - *Pros:* Deterministic, entirely stateless.
    - *Cons:* Inevitable collisions require expensive DB retry loops (salting).

### 2. Scaling Reads for Instant Redirects
Handling 600,000 reads per second requires aggressive optimization at multiple layers:
- **In-Memory Caching:** Introduce a Redis or Memcached cluster (using LRU eviction) between the Read Service and the DB. Memory access is orders of magnitude faster than SSD, absorbing the bulk of redirect traffic.
- **Database Indexing:** Ensure a B-tree index is placed on the `short_code` column to prevent full table scans and provide $\mathcal{O}(\log n)$ DB lookups on cache misses.
- **CDNs & Edge Computing:** Deploy the redirect logic directly to the edge. A CDN caches mappings globally, resolving requests near the user without ever touching origin servers.

### 3. Analytics via MapReduce
Since real-time analytics aren't required, we MapReduce the web server logs offline to protect the read path.
- **Mapper:** Parses each log line, extracting the `period` (e.g., 2026-03) and `url`. Yields key-value pairs: `((2026-03, url1), 1)`.
- **Reducer:** Sums the values for each key: `yield key, sum(values)`.

### ⚖️ Trade-offs

| Decision | Pros | Cons / Limitations |
| :--- | :--- | :--- |
| **301 vs 302 HTTP Redirect** | **301 (Permanent)** caches the redirect in the user's browser, vastly reducing server load. | **302 (Temporary)** is preferred because it forces the browser to hit the server, enabling analytics tracking and allowing links to expire cleanly. |
| **SQL vs NoSQL (Key-Value)** | SQL provides easy secondary indexes (like sorting by `created_at` for expiration cleanup). | NoSQL scales horizontally natively for massive read/write volumes. |
| **Base62 vs Base64** | Base62 (`A-Z, a-z, 0-9`) allows exactly 6-7 characters to represent billions of URLs cleanly without URL-escaping. | Base64 includes `+` and `/` characters, which can break URL routing if not strictly URL-safe encoded. |

---

## 🚨 Edge Cases
- **Infinite Redirect Loops:** Validate domain to ensure the submitted URL does not point back to your own shortener.
- **Custom Alias Collisions:** Maintain a separate namespace or prefix for custom aliases to prevent colliding with auto-generated Base62 codes.
- **Expired Links:** Return `410 Gone`. Ensure cache TTL matches URL expiration so stale links don't survive in memory.
- **Abuse/Spam:** Implement rate limiting and malicious URL filtering (e.g., Google Safe Browsing API) prior to shortlink generation.

---

## 🎤 Interview Toolkit

- **Scale Question:** "A celebrity link goes viral and gets 100,000 clicks a second. How do you survive?" -> *Rely on the cache-first read path. A properly tuned Redis cluster handles hundreds of thousands of reads per second. Ensure the Load Balancer routes traffic effectively, use a CDN to absorb global traffic, and implement an L1 in-memory cache (like Guava) on the Web Servers themselves for extreme hot-keys.*
- **Failure Probe:** "What happens if the Redis counter or Key Generation Service (KGS) crashes?" -> *Since App Servers keep a batch of thousands of keys in their local RAM, they can continue serving write requests for several minutes while the KGS/Redis is restarted via automatic failover (e.g., Redis Sentinel).*
- **Cleanup Question:** "How do you delete expired URLs efficiently?" -> *Rely primarily on TTL in the Redis cache. For the persistent database, run a background cleanup cron job (e.g., daily during off-peak hours) to delete expired rows sequentially, rather than checking expiration timestamps on every active read.*

## 🧩 Key Design Insights
* **Reads dominate** $\rightarrow$ optimize cache.
* **Writes are rare** $\rightarrow$ optimize correctness & consistency.
* **Keep hot path minimal** $\rightarrow$ push heavy work async (MapReduce analytics, Cron cleanup).

## 🔗 Related Architectures
- [Machine Coding: Cache System](../../../machine_coding/systems/cache/PROBLEM.md) — Excellent for understanding the LRU mechanisms protecting the DB.
- [System Design: Twitter Feed (Snowflake ID)](../social_media/TWITTER_HLD.md) — Alternative method for generating unique distributed IDs.
- [System Design: API Rate Limiter](../utilities/RATE_LIMITER.md) — Preventing spam abuse in the system.
