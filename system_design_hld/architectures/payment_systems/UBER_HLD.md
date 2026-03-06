# HLD: Design a Ride-Sharing Global Matcher (Uber Global)

## 🚀 Problem Statement
Design the high-level architecture for a system that matches millions of riders with drivers globally while handling dynamic pricing and real-time location updates.

## 🛠️ Functional Requirements
1. **Location Tracking:** High-frequency updates from millions of driver apps.
2. **Matching:** Match rider to driver in < 5 seconds.
3. **Dynamic Pricing:** Surge calculation based on hexagonal cell density.

## 📈 Non-Functional Requirements
1. **Write-Heavy Load:** Constant location pings.
2. **Partition Tolerance:** The system must function locally even if global links are down.

## 🧠 Key Design Challenges (5YOE Focus)
- **Geospatial Indexing:** Quadtrees vs Google S2 vs Uber H3. Why one over the other?
- **Consistency:** How to prevent two riders from being matched to the same driver simultaneously?
- **Handling Flash Crowds:** Concerts or sports events causing massive localized demand spikes.
