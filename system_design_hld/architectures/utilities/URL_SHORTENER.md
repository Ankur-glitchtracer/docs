# 🔗 System Design: URL Shortener (TinyURL)

## 📝 Overview
A **URL Shortener** is a service that creates short, unique aliases for long URLs. Its primary goal is to provide a compact link that is easy to share while ensuring rapid redirection to the original destination, even under extreme read loads.

!!! abstract "Core Concepts"

    - **Base62 Encoding:** Converting a unique numeric ID into a compact 7-character string using `[a-zA-Z0-9]`.
    - **Unique ID Generation:** Using distributed systems like Snowflake or database sequences to guarantee uniqueness without coordination overhead.
    - **Heavy-Read Optimization:** Utilizing intensive caching (Redis) for the most popular links to handle the high read-to-write ratio.

## 🛠️ Functional & Non-Functional Requirements
### Functional Requirements

1. **URL Shortening:** Accept a long URL and return a unique 7-character alias.
2. **Redirection:** Redirect short URL requests to the original long URL with minimal latency.
3. **Custom Aliases:** Allow users to provide their own custom short aliases.

### Non-Functional Requirements

1. **High Availability:** The redirection service must be 99.999% available (it's useless if links don't work).
2. **Low Latency:** Redirects should happen in under 100ms.
3. **Unpredictability:** Shortened URLs should not be easily guessable to prevent bulk scraping of data.

## 🧠 The Engineering Story

**The Villain:** "The Duplicate Key." You use a random 7-character string for every URL. After 1 billion URLs, the chance of a collision (two URLs getting the same ID) becomes a certainty, breaking the web.

**The Hero:** "The Distributed Counter (Base62)." Using a unique 64-bit ID from a central generator (like Snowflake or a DB auto-increment) and encoding it into `a-zA-Z0-9`.

**The Plot:**

1. **ID Generation:** Get a unique number (e.g., `1234567`).
2. **Encoding:** Convert the number to Base62 (e.g., `8cb`).
3. **Storage:** Map `8cb` -> `https://long-url.com` in a KV store.
4. **Caching:** Cache the top 1% of URLs to handle 90% of traffic.

**The Twist (Failure):** **The Prediction Attack.** If you use sequential IDs, a competitor can script a crawl of every URL you've ever shortened by just incrementing the ID.

**Interview Signal:** mastery of **Unique ID Generation**, **Encoding vs Hashing**, and **Read-Heavy Caching**.

## 🏗️ High-Level Architecture
Design a service that converts long URLs into short, 7-character aliases (e.g., `bit.ly/xyz123`).

### Key Design Challenges:
#### Capacity Planning (Back-of-the-envelope)

- **Traffic:** 100M new URLs per month.
- **Read/Write Ratio:** 100:1 (Heavy reads).
- **Storage:** 100M * 500 bytes = 5GB per month. 10 years = 600GB.
- **QPS:** ~40 write QPS, ~4000 read QPS.

#### Technical Challenges

- **Key Generation:** Base62 encoding vs. MD5 hashing.
- **Scaling Reads:** Using a cache (Redis) for the top 20% of URLs.
- **Database Choice:** Deciding between NoSQL (DynamoDB/Cassandra) for horizontal scale and SQL for structured management.
- **Redirection Latency:** Minimizing the round-trip time for the redirect.

## 🔍 Deep Dives
(To be detailed...)

## 📊 Data Modeling & API Design
### Data Model

- **(To be detailed...)**: (To be detailed...)

### API Design

- **(To be detailed...)**: (To be detailed...)

## 📈 Scalability & Bottlenecks
(To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** (To be detailed...)
- **Scale Question:** (To be detailed...)
- **Edge Case Probe:** (To be detailed...)

## 🔗 Related Architectures

- [Rate Limiter](./RATE_LIMITER.md) — For link creation throttling.
