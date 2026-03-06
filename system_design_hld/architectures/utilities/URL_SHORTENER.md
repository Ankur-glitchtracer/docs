# HLD: Design a URL Shortener (TinyURL)

## 🚀 Problem Statement
Design a service that converts long URLs into short, 7-character aliases (e.g., `bit.ly/xyz123`).

## 📈 Capacity Planning (Back-of-the-envelope)
- **Traffic:** 100M new URLs per month.
- **Read/Write Ratio:** 100:1 (Heavy reads).
- **Storage:** 100M * 500 bytes = 5GB per month. 10 years = 600GB.
- **QPS:** ~40 write QPS, ~4000 read QPS.

## 🧠 Key Design Challenges
- **Key Generation:** Base62 encoding vs. MD5 hashing.
- **Scaling Reads:** Using a cache (Redis) for the top 20% of URLs.
- **Database:** Is a NoSQL Key-Value store (DynamoDB/Cassandra) better than SQL for this scale?
- **Redirection Latency:** Minimizing the round-trip time for the redirect.
