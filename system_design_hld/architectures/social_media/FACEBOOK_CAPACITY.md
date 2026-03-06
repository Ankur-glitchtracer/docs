# HLD: Facebook-Scale Capacity Planning

## 🚀 The Scenario
Perform a back-of-the-envelope estimation for a platform with 2 Billion Daily Active Users (DAU).

## 📊 The Computation Tasks
### 1. Storage Computation
- **Scenario:** Users upload 500M photos/day. Average photo size = 200KB.
- **Task:** Calculate total storage per day and per year (including 3x replication).

### 2. RAM Estimation
- **Scenario:** We want to cache 20% of the daily metadata read requests.
- **Task:** Estimate total RAM needed for the Redis cluster.

### 3. Server Count
- **Scenario:** Each web server can handle 5000 concurrent requests. Peak traffic is 500k requests/sec.
- **Task:** Estimate no. of web servers needed.
