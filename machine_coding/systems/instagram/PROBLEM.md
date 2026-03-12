# 📸 Machine Coding: Instagram-Lite Social Feed

## 📝 Overview
Design a simplified **Social Media Feed** system. This challenge focuses on relationship management (following), content creation, and the algorithmic generation of a personalized user feed.

!!! info "Why This Challenge?"

    - **Scalable Event Propagation:** Learning how to handle the "Fan-out" problem when a celebrity with millions of followers posts content.
    - **Relationship Management:** Understanding how to represent and traverse a large graph of user relationships (following/followers).
    - **Feed Aggregation:** Mastering the merging and sorting of content from multiple sources into a real-time chronological timeline.

!!! abstract "Core Concepts"

    - **Graph Relationships:** Managing a "Following" graph to determine content visibility.
    - **Feed Aggregation:** Combining and sorting posts from multiple sources into a single, cohesive timeline.

## 🛠️ Requirements & Technical Constraints
### Functional Requirements

1.  **User Profiles:** Create and manage user profiles.
2.  **Follow/Unfollow:** Support bidirectional relationship management.
3.  **Posting Content:** Allow users to create posts with text/images.
4.  **Home Feed:** Generate a personalized feed of posts from followed users.

### Technical Constraints

- **Chronological Sorting:** Posts in the feed must be strictly ordered from newest to oldest.
- **Data Integrity:** Ensure that unfollowing a user immediately removes their future posts from the follower's feed.
- **Performance:** Feed generation should be fast even for users following thousands of people.

## 🧠 The Engineering Story

**The Villain:** "The Fan-out Explosion." A celebrity with 1M followers posts a photo. If you try to update 1M feeds simultaneously, your database locks up and the app crashes.

**The Hero:** "The Hybrid Feed Model." Pull for celebrities, push for regular users.

**The Plot:**

1. Store `Users` and their `Follow` relationships.
2. Maintain a `Post` repository.
3. Use the **Observer Pattern** to notify active followers.
4. Merge and sort posts chronologically in the `FeedManager`.

**The Twist (Failure):** **The Ghost Follow.** If a user unfollows another, but their old posts still appear in the feed due to stale caches.

**Interview Signal:** Understanding of **Event-Driven Architecture** and **Scalable Feed Generation**.

## 🚀 Thinking Process & Approach
Social feeds are a massive data synchronization problem. The approach uses the Observer pattern to push updates to followers and a caching layer to generate personalized feeds efficiently.

### Key Observations:

- Scalable event propagation.
- Personalized feed generation logic.

## 🏗️ Design Patterns Used

- **Observer Pattern**: To push new posts to the feeds of all active followers (Fan-out on write).
- **Iterator Pattern**: To provide a clean way to traverse through a user's feed with pagination.
- **Strategy Pattern**: For implementing different feed ranking algorithms (Chronological, Relevance, Popularity).
- **Singleton/Factory Pattern**: For managing the global Post and User repositories.

## 💻 Solution Implementation

```python
--8<-- "machine_coding/systems/instagram/social_media_feed.py"
```

!!! success "Why this works"
    This design adheres to the Open/Closed principle and ensures high maintainability by decoupling concerns.

## 🎤 Interview Follow-ups

- **Celebrity Problem:** How do you handle the feed generation for a user following 100 "celebrities" (Push vs Pull model)?
- **Media Optimization:** How would you handle the storage and delivery of high-resolution images/videos (CDN, Image Compression)?
- **Real-time Updates:** How would you implement "Pull-to-refresh" or "Live" updates in the feed using WebSockets?

## 🔗 Related Challenges

- [Persistent Pub-Sub](../../distributed/pub_sub/PROBLEM.md) — For a generic event broadcasting system.
- [High-Performance Cache](../cache_system/PROBLEM.md) — For caching personalized user feeds to improve latency.
