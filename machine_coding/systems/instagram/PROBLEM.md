# 📸 Machine Coding: Instagram-Lite Social Feed

## 📝 Overview
Design a simplified **Social Media Feed** system. This challenge focuses on relationship management (following), content creation, and the algorithmic generation of a personalized user feed.

!!! abstract "Core Concepts"
    - **Graph Relationships:** Managing a "Following" graph to determine content visibility.
    - **Feed Aggregation:** Combining and sorting posts from multiple sources into a single, cohesive timeline.

## 🚀 Problem Statement
Build the backend for a social platform where users can post content and follow others. The primary goal is to generate a "Home Feed" for each user that displays recent posts from everyone they follow, sorted chronologically.

## 🧠 Thinking Process & Approach
Social feeds are a massive data synchronization problem. The approach uses the Observer pattern to push updates to followers and a caching layer to generate personalized feeds efficiently.

### Key Observations:
- Scalable event propagation.
- Personalized feed generation logic.

### Technical Constraints
- **Chronological Sorting:** Posts in the feed must be strictly ordered from newest to oldest.
- **Data Integrity:** Ensure that unfollowing a user immediately removes their future posts from the follower's feed.

