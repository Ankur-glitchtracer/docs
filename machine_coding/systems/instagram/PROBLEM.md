# 📸 Machine Coding: Instagram-Lite Social Feed

## 📝 Overview
Design a simplified **Social Media Feed** system. This challenge focuses on relationship management (following), content creation, and the algorithmic generation of a personalized user feed.

!!! abstract "Core Concepts"
    - **Graph Relationships:** Managing a "Following" graph to determine content visibility.
    - **Feed Aggregation:** Combining and sorting posts from multiple sources into a single, cohesive timeline.

## 🚀 Problem Statement
Build the backend for a social platform where users can post content and follow others. The primary goal is to generate a "Home Feed" for each user that displays recent posts from everyone they follow, sorted chronologically.

### Technical Constraints
- **Chronological Sorting:** Posts in the feed must be strictly ordered from newest to oldest.
- **Data Integrity:** Ensure that unfollowing a user immediately removes their future posts from the follower's feed.

## 🛠️ Requirements
1.  **User Management:** Support `follow(user_id)` and `unfollow(user_id)` actions.
2.  **Post Creation:** Users can create posts with a caption and an optional media link.
3.  **Feed Generation:** A `get_feed(user_id)` method that returns a personalized list of posts.
4.  **Performance:** Consider the "Fan-out" problem when a celebrity with millions of followers makes a post.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/systems/instagram/social_media_feed.py"
```

!!! success "Why this works"
    The system uses a decoupled approach where user relationships and post data are managed independently. This allows the feed generator to act as a query engine that aggregates data from the graph, providing a flexible foundation for more complex ranking algorithms later.
