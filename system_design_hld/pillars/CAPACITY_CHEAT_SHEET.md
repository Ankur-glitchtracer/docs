# Capacity Estimation & System Constraints Cheat Sheet

This document serves as a master reference for **real-world capacity estimations**, **read/write ratios**, and **latency targets** extracted from production-scale architectures.

---

## 1. Global Latency & Performance Targets

| System | Operation | Latency Target |
|---|---|---|
| Twitter | Timeline Generation | < 200 ms |
| Instagram | News Feed Generation | < 200 ms |
| Facebook | Feed Generation (End-User) | < 2.0 seconds |
| Facebook | Post Propagation to Followers | < 5.0 seconds |
| Typeahead / Search | Autocomplete Suggestions | < 200 ms (with 50 ms client debounce) |

---

## 2. Traffic and Read:Write Ratios

Understanding the **symmetry of a system** dictates the **database choice** and **caching strategy**.

| System Profile | Read:Write Ratio | Daily Active Users (DAU) | Traffic Volume |
|---|---|---|---|
| Twitter | 280:1 (Extremely Read Heavy) | 200 Million | 100M writes/day vs 28B reads/day |
| YouTube / Netflix | 200:1 (Read Heavy) | 800 Million | 500 hrs uploaded/min vs 46K views/sec |
| URL Shortener | 100:1 (Read Heavy) | N/A | 500M writes/month vs 50B reads/month |
| Pastebin | 5:1 (Read Heavy) | N/A | 1M writes/day vs 5M reads/day |
| Dropbox / Google Drive | 1:1 (Balanced) | 100 Million | 1M active connections/minute |

---

## 3. Storage & Memory Estimations

Specific **byte-level constraints** required for sizing distributed databases and caches.

### Social Media & Chat

**Twitter Storage**

- 140 chars = **280 bytes**
- Metadata ≈ **30 bytes**
- Total ≈ **310 bytes per tweet**

Estimates:

- **Text storage:** ~30 GB/day  
- **Media storage:** ~24 TB/day  

---

**Instagram Storage**

- User record = **68 bytes**
- Photo metadata = **284 bytes**
- UserFollow record = **8 bytes**

Estimate:

- **Total relational DB size for 10 years:** ~3.7 TB

---

**Facebook Feed Cache**

To keep **top 500 posts (1 KB each)** in memory for **300M DAU**:

- Memory required ≈ **150 TB RAM**
- Infrastructure ≈ **1,500 machines** with **100 GB RAM each**

---

**Facebook Messenger**

- **100 bytes/message**
- **20 Billion messages/day**

Estimates:

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

---

**Uber (Driver Tracking)**

Driver location record:

- DriverID = **3 bytes**
- Old coordinates = **16 bytes**
- New coordinates = **16 bytes**

Total = **35 bytes per driver**

Estimate:

- **1M drivers in memory:** ~35 MB

---

### Rate Limiting Systems

**API Rate Limiter (Fixed Window)**

- **32 bytes per user**
- **1M users tracked:** ~32 MB RAM

---

**API Rate Limiter (Sliding Window Log)**

- **12 KB per user**
- **1M users tracked:** ~12 GB RAM
