# 🐦 System Design: Twitter

## 📝 Overview
Twitter is a massive, globally distributed microblogging and social networking service defined by extreme read-heavy traffic and real-time data propagation. It enables users to broadcast short text messages and media to followers instantly, requiring a highly optimized architecture to solve the complex "celebrity problem" of viral distribution.

!!! abstract "Core Concepts"
    - **Scatter-Gather (Pull Model):** Aggregating a user's timeline at runtime by querying multiple database shards.
    - **Fan-out on Write (Push Model):** Pre-computing and pushing tweets to followers' cached timelines to ensure low read latency.
    - **Snowflake IDs:** Generating globally unique, chronologically sortable 64-bit integers without centralized bottlenecks.

---

## 🏭 The Scenario & Requirements

### 😡 The Problem (The Villain)
Retrieving chronologically sorted feeds for a user who follows thousands of people requires massive database JOINs or multi-shard queries. Furthermore, when a "Hot User" (a celebrity with 50 million followers) posts, updating 50 million feeds simultaneously can melt traditional database and caching layers.

### 🦸 The Solution (The Hero)
A hybrid fan-out architecture that pushes tweets to active followers for normal users, but forces clients to pull tweets dynamically from celebrities. This is paired with an ingenious 64-bit ID generation scheme (Snowflake) that embeds timestamps directly into the Tweet ID, eliminating the need for expensive secondary chronological indices.

### 📜 Requirements
- **Functional Requirements:**
    1. Users can post tweets (text and media).
    2. Users can follow/unfollow other users.
    3. Users can view their Home Timeline (an aggregated, chronologically sorted feed of everyone they follow).
- **Non-Functional Requirements:**
    1. **High Availability:** The system must never go down (Eventual consistency for timelines is highly acceptable).
    2. **Low Read Latency:** Home timeline generation must render in < 200ms.
    3. **Scalability:** Must handle extreme read/write skew and viral load spikes gracefully.

!!! info "Capacity Estimation (Back-of-the-envelope)"
    - **Traffic:** 300M Daily Active Users (DAU). 50M writes (tweets) per day. 5 Billion reads (timeline requests) per day. -> **100:1 Read/Write ratio**.
    - **Storage (Text):** 50M tweets * 200 bytes = 10GB/day = ~3.6TB/year.
    - **Storage (Media):** Assume 20% of tweets contain a 1MB image/video. 10M * 1MB = 10TB/day = ~3.6PB/year.
    - **Bandwidth:** 10TB / 86400s = ~115 MB/s sustained write throughput.

---

## 📊 API Design & Data Model

=== "REST APIs"
    - **`POST /api/v1/tweets`**
        - **Request:** `{ "text": "Hello World!", "media_ids": [...] }`
        - **Response:** `{ "tweet_id": "123456789012345678", "created_at": "..." }`
    - **`GET /api/v1/timelines/home`**
        - **Query Params:** `?limit=20&max_id=123456789012345678`
        - **Response:** `[ { "tweet_id": "...", "text": "...", "author": {...} }, ... ]`
    - **`POST /api/v1/users/{user_id}/follow`**
        - **Response:** `200 OK`

=== "Database Schema"
    - **Table:** `tweets` (Cassandra / Sharded RDBMS)
        - `tweet_id` (BigInt, PK) - Snowflake ID
        - `user_id` (BigInt, Indexed)
        - `content` (Varchar/Text)
        - `created_at` (Timestamp)
    - **Table:** `follows` (RDBMS or Graph DB)
        - `follower_id` (BigInt, PK)
        - `followee_id` (BigInt, PK)
        - *Compound Primary Key (follower_id, followee_id)*
    - **Cache:** `user_timeline` (Redis)
        - `Key:` `timeline:{user_id}`
        - `Value:` `List<tweet_id>` (Bounded to max 800 recent tweets)

---

## 🏗️ High-Level Architecture

### Architecture Diagram
```mermaid
graph TD
    Client[Client App] -->|HTTP/HTTPS| CDN[CDN]
    CDN --> |API Calls| API_GW[API Gateway / Load Balancer]
    
    API_GW --> TweetSvc[Tweet Service]
    API_GW --> TimelineSvc[Timeline Service]
    API_GW --> UserSvc[User Service]
    
    TweetSvc --> IDGen[Snowflake ID Generator]
    TweetSvc --> Fanout[Fan-out Workers]
    
    Fanout -.-> RedisCache[(Redis Timeline Cache)]
    TimelineSvc --> RedisCache
    
    TweetSvc --> DB_Tweets[(Tweet DB Cluster)]
    UserSvc --> DB_Users[(User/Graph DB)]
    
    TimelineSvc -.-> DB_Tweets
````

### Component Walkthrough

1.  **API Gateway & CDN:** Serves static media from edge nodes and routes dynamic API requests to internal microservices.
2.  **Tweet Service:** Handles the ingress of new tweets, requests a unique ID from the Snowflake generator, and persists the data.
3.  **Fan-out Workers (Asynchronous):** Background processes (Kafka consumers) that fetch a user's followers and push the new `tweet_id` into their Redis timeline caches.
4.  **Timeline Service:** Serves the actual feed. It first checks the Redis Cache for pre-computed timelines. If missing, it falls back to a scatter-gather query against the Tweet DB.
5.  **Snowflake ID Generator:** Dedicated microservices returning 64-bit integers ensuring chronologically sortable unique keys.

-----

## 🔬 Deep Dive & Scalability

### Handling Bottlenecks: The Core Trade-off

When generating a timeline, the system must retrieve the most recent tweets from every user the client follows.

#### Approach A: Sharding by UserID (The Flawed Approach)

If the database is partitioned by UserID, all of a single user's tweets are stored on the same physical server.

  - **The Downside (The Celebrity Problem):** If a celebrity with 50 million followers posts a tweet, millions of read requests instantly hit the single server holding that UserID, causing immediate resource starvation.

#### Approach B: Sharding by TweetID (The Optimized Approach)

Twitter hashes the TweetID itself to determine the partition.

  - **The Upside:** Neutralizes the "hot user" bottleneck. Write and read traffic are perfectly distributed across the entire cluster.
  - **The Downside (Scatter-Gather):** Retrieving a timeline requires a complex network fan-out operation.

#### Chronological Sharding & 64-Bit TweetIDs

Twitter eliminates the need for expensive secondary timestamp indices by embedding chronological data directly into the primary key (Snowflake ID).

  - **Timestamp (41 bits):** Epoch timestamp in millisecond precision (good for 69 years). *Note: Adjusted bits for standard Snowflake implementation.*
  - **Machine ID (10 bits):** Identifies the specific worker machine (up to 1024 machines).
  - **Sequence (12 bits):** Auto-incrementing sequence to prevent collisions within the exact same millisecond (4096 IDs per ms per machine).

Because time occupies the leading bits, any list of TweetIDs sorted numerically is automatically sorted chronologically.

### The Scatter-Gather Timeline Generation (Pull Model)

When a client requests their timeline under the TweetID sharding model (often used as a fallback or for celebrities), the system executes a Scatter-Gather fanout.

```mermaid
sequenceDiagram
    participant Client
    participant Aggregator as Timeline Service
    participant DB1 as Partition 1
    participant DB2 as Partition 2

    Client->>Aggregator: Request Timeline
    Note over Aggregator: Retrieves Followed Users
    Aggregator->>DB1: Broadcast Query (Get latest from Followed)
    Aggregator->>DB2: Broadcast Query (Get latest from Followed)
    
    Note over DB1,DB2: Local sort by Recency (O(1) due to Snowflake)
    
    DB1-->>Aggregator: Return Local Top Tweets
    DB2-->>Aggregator: Return Local Top Tweets
    
    Note over Aggregator: Merge datasets & Global Sort
    Aggregator-->>Client: Return complete timeline
```

### ⚖️ Trade-offs

| Decision | Pros | Cons / Limitations |
| :--- | :--- | :--- |
| **Push Model (Fan-out on Write)** | Instant timeline reads (O(1) cache lookup). Great for standard users. | Massive write amplification. A celebrity tweet takes minutes to push to 50M Redis lists. |
| **Pull Model (Fan-out on Read)** | Zero write amplification. Tweet is saved instantly. Great for celebrities. | High read latency and complex aggregation logic at runtime (Scatter-Gather). |
| **Hybrid Approach** | Best of both worlds. Push for normal users, Pull for celebrities. | Increased system complexity. Requires tracking "hot" users and maintaining dual-read logic in the Timeline Service. |

-----

## 🎤 Interview Toolkit

  - **Scale Question:** "Justin Bieber posts a tweet. How do you prevent the system from crashing?" -\> *Use a Hybrid Fan-out. Bieber is marked as a 'celebrity'. His tweets are NOT pushed to followers' Redis queues. Instead, when a follower opens their app, the Timeline Service pulls their pre-computed Redis queue, separately pulls Bieber's recent tweets from the DB/Cache, merges them in memory, and returns the result.*
  - **Failure Probe:** "What happens if a Redis cache node containing 10,000 user timelines goes down?" -\> *Use Consistent Hashing to minimize reshuffling. Rebuild the lost feeds asynchronously using the Scatter-Gather Pull model from the persistent Tweet DB upon the next user request.*
  - **Edge Case:** "How do you handle pagination in a rapidly changing feed?" -\> *Never use offset-based pagination (`OFFSET 100`). New tweets will shift the offset, causing users to see duplicate tweets. Use cursor-based pagination using the Snowflake `tweet_id` (e.g., `WHERE tweet_id < {last_seen_id}`).*

## 🔗 Related Architectures

  - [Design Instagram (Newsfeed)](./INSTAGRAM_HLD.md) — Highly visual, read-heavy, similar timeline aggregation.
  - [Design Facebook Newsfeed](./FACEBOOK_NEWSFEED.md) — EdgeRank algorithm heavy, complex privacy checks during fan-out.
  - [Machine Coding: Instagram Feed](../../../machine_coding/systems/instagram/PROBLEM.md)
  - [DSA: Design Twitter (K-Way Merge)](../../../dsa/09_heap_priority_queue/design_twitter/PROBLEM.md)
