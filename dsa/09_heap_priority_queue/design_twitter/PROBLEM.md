#  🐦 Heap: Design Twitter

## 📝 Description
[LeetCode 355](https://leetcode.com/problems/design-twitter/)
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The Feed Merger." A user follows 100 people. Each has posted 10,000 tweets. Generating a timeline of the top 10 most recent tweets efficiently is hard. Sorting 1 million tweets ($O(M \log M)$) is too slow.

**The Hero:** "The K-Way Merge (Min-Heap)." This is exactly like **Merge K Sorted Lists**.

**The Plot:**

1. **Data Model:**
   - `User`: ID, Set of Followees.
   - `Tweet`: ID, Timestamp (global counter), Next Tweet (LinkedList style for user history).
   - `TweetMap`: UserID -> Head of Tweet List.
2. **GetNewsFeed:**
   - Gather head tweets of all followees.
   - Push to Max-Heap (ordered by time).
   - Pop 10 times. When popping a tweet, push its `next` tweet into the heap.

**The Twist (Failure):** **Scalability.** In a real system, you'd Fan-Out on Write (push to followers' feeds). But for this problem, Fan-Out on Read (pull) is the expected solution.

**Interview Signal:** System Design basics implemented with **OO Principles**.

## 🚀 Approach & Intuition
Pull-based feed generation.

### C++ Pseudo-Code
```cpp
class Twitter {
    struct Tweet {
        int id;
        int time;
        Tweet* next = nullptr;
        Tweet(int i, int t) : id(i), time(t) {}
    };
    
    unordered_map<int, Tweet*> tweets;
    unordered_map<int, unordered_set<int>> following;
    int time = 0;
    
public:
    void postTweet(int userId, int tweetId) {
        Tweet* t = new Tweet(tweetId, time++);
        t->next = tweets[userId];
        tweets[userId] = t;
    }
    
    vector<int> getNewsFeed(int userId) {
        priority_queue<pair<int, Tweet*>> pq;
        // Add self
        if (tweets[userId]) pq.push({tweets[userId]->time, tweets[userId]});
        // Add followees
        for (int fId : following[userId]) {
            if (tweets[fId]) pq.push({tweets[fId]->time, tweets[fId]});
        }
        
        vector<int> res;
        while (!pq.empty() && res.size() < 10) {
            auto top = pq.top(); pq.pop();
            res.push_back(top.second->id);
            if (top.second->next) 
                pq.push({top.second->next->time, top.second->next});
        }
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        following[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        following[followerId].erase(followeeId);
    }
};
```

### Key Observations:

- Heaps are the go-to for finding the $K$-th largest or smallest element in $O(N \log K)$ time.
- Use a Min-Heap for $K$ largest elements and a Max-Heap for $K$ smallest elements to optimize space.

!!! info "Complexity Analysis"

    - **Time Complexity:** Post: $O(1)$, GetFeed: $O(10 \log F)$ where F is number of followees.
    - **Space Complexity:** $O(U + T)$ users and tweets.

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you implement a custom Heap from scratch? How would you implement a 'Decrease Key' operation?
- **Scale Question:** How would you maintain a Top-K list across 100 machines with frequent updates?
- **Edge Case Probe:** What if all elements have the same priority? How do you handle empty heap extractions?

## 🔗 Related Problems

- [Find Median from Stream](../find_median_from_data_stream/PROBLEM.md) — Next in category
- [Task Scheduler](../task_scheduler/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Maximum Subarray](../../15_greedy/maximum_subarray/PROBLEM.md) — Prerequisite for Greedy
