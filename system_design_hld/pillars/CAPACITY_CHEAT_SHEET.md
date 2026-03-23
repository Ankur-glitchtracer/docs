# Capacity Estimation & System Constraints Cheat Sheet

This document serves as a master reference for **real-world capacity estimations**, **read/write ratios**, and **latency targets** extracted from production-scale architectures. 

Use the foundational quick-reference tables at the top to drive your math during the back-of-the-envelope estimation phase of a system design interview.

---

## 1. Quick Reference: Powers of Two

| Power | Exact Value | Approx Value | Bytes |
| :--- | :--- | :--- | :--- |
| **7** | 128 | - | - |
| **8** | 256 | - | - |
| **10** | 1,024 | 1 thousand | 1 KB |
| **16** | 65,536 | - | 64 KB |
| **20** | 1,048,576 | 1 million | 1 MB |
| **30** | 1,073,741,824 | 1 billion | 1 GB |
| **32** | 4,294,967,296 | - | 4 GB |
| **40** | 1,099,511,627,776 | 1 trillion | 1 TB |

---

## 2. Fundamental Latency & Throughput Numbers

| Operation | Time (ns) | Time (μs / ms) | Notes |
| :--- | :--- | :--- | :--- |
| **L1 cache reference** | 0.5 ns | | |
| **Branch mispredict** | 5 ns | | |
| **L2 cache reference** | 7 ns | | 14x L1 cache |
| **Mutex lock/unlock** | 25 ns | | |
| **Main memory reference** | 100 ns | | 20x L2 cache, 200x L1 cache |
| **Compress 1K bytes with Zippy** | 10,000 ns | 10 μs | |
| **Send 1 KB bytes over 1 Gbps network** | 10,000 ns | 10 μs | |
| **Read 4 KB randomly from SSD** | 150,000 ns | 150 μs | ~1 GB/sec SSD |
| **Read 1 MB sequentially from memory** | 250,000 ns | 250 μs | |
| **Round trip within same datacenter** | 500,000 ns | 500 μs | |
| **Read 1 MB sequentially from SSD** | 1,000,000 ns | 1 ms | ~1 GB/sec SSD, 4x memory |
| **HDD seek** | 10,000,000 ns | 10 ms | 20x datacenter roundtrip |
| **Read 1 MB sequentially from 1 Gbps** | 10,000,000 ns | 10 ms | 40x memory, 10x SSD |
| **Read 1 MB sequentially from HDD** | 30,000,000 ns | 30 ms | 120x memory, 30x SSD |
| **Send packet CA -> Netherlands -> CA** | 150,000,000 ns | 150 ms | |

!!! info "Handy Conversions & Throughput Metrics"
    **Time Conversions:**
    
    * 1 ns = $10^{-9}$ seconds
    * 1 μs = $10^{-6}$ seconds = 1,000 ns
    * 1 ms = $10^{-3}$ seconds = 1,000 μs = 1,000,000 ns
    
    **Throughput Capacities:**
    
    * **HDD Sequential Read:** ~30 MB/s
    * **1 Gbps Ethernet Sequential Read:** ~100 MB/s
    * **SSD Sequential Read:** ~1 GB/s
    * **Main Memory Sequential Read:** ~4 GB/s
    
    **Network Boundaries:**
    
    * **Datacenter Network:** ~2,000 round trips per second
    * **Global Network:** ~6-7 world-wide round trips per second

---

## 3. Global Latency & Performance Targets

| System | Operation | Latency Target |
| :--- | :--- | :--- |
| **Twitter** | Timeline Generation | < 200 ms |
| **Instagram** | News Feed Generation | < 200 ms |
| **Facebook** | Feed Generation (End-User) | < 2.0 seconds |
| **Facebook** | Post Propagation to Followers | < 5.0 seconds |
| **Typeahead / Search** | Autocomplete Suggestions | < 200 ms (with 50 ms client debounce) |

---

## 4. Traffic and Read:Write Ratios

Understanding the **symmetry of a system** dictates the **database choice** and **caching strategy**.

| System Profile | Read:Write Ratio | Daily Active Users (DAU) | Traffic Volume |
| :--- | :--- | :--- | :--- |
| **Twitter** | 280:1 (Extremely Read Heavy) | 200 Million | 100M writes/day vs 28B reads/day |
| **YouTube / Netflix** | 200:1 (Read Heavy) | 800 Million | 500 hrs uploaded/min vs 46K views/sec |
| **URL Shortener** | 100:1 (Read Heavy) | N/A | 500M writes/month vs 50B reads/month |
| **Pastebin** | 5:1 (Read Heavy) | N/A | 1M writes/day vs 5M reads/day |
| **Dropbox / Google Drive** | 1:1 (Balanced) | 100 Million | 1M active connections/minute |

---

## 5. Storage & Memory Estimations

Specific **byte-level constraints** required for sizing distributed databases and caches.

### Social Media & Chat

**Twitter Storage**

- 140 chars = **280 bytes**
- Metadata ≈ **30 bytes**
- Total ≈ **310 bytes per tweet**

*Estimates:*
- **Text storage:** ~30 GB/day  
- **Media storage:** ~24 TB/day  

**Instagram Storage**

- User record = **68 bytes**
- Photo metadata = **284 bytes**
- UserFollow record = **8 bytes**

*Estimates:*
- **Total relational DB size for 10 years:** ~3.7 TB

**Facebook Feed Cache**

To keep the **top 500 posts (1 KB each)** in memory for **300M DAU**:

- Memory required ≈ **150 TB RAM**
- Infrastructure ≈ **1,500 machines** with **100 GB RAM each**

**Facebook Messenger**

- **100 bytes/message**
- **20 Billion messages/day**

*Estimates:*
- **Storage/day:** ~2 TB
- **5-year history:** ~3.6 PB

---

### Geospatial & Utilities

**Yelp (QuadTree Index)**

- **500M places**
- ~**1M leaf nodes**

Caching **LocationID + Lat + Long (24 bytes)**:

- Memory required ≈ **12 GB RAM**
- Tree pointer overhead ≈ **10 MB**

**Uber (Driver Tracking)**

Driver location record:

- DriverID = **3 bytes**
- Old coordinates = **16 bytes**
- New coordinates = **16 bytes**

*Total* = **35 bytes per driver**

*Estimates:*
- **1M drivers in memory:** ~35 MB

---

### Rate Limiting Systems

**API Rate Limiter (Fixed Window)**

- **32 bytes per user**
- **1M users tracked:** ~32 MB RAM

**API Rate Limiter (Sliding Window Log)**

- **12 KB per user**
- **1M users tracked:** ~12 GB RAM
