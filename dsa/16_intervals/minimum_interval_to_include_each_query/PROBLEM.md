#  🎯 Intervals: Minimum Interval to Include Each Query

## 📝 Description
[LeetCode 1851](https://leetcode.com/problems/minimum-interval-to-include-each-query/)
You are given a 2D integer array `intervals`, where `intervals[i] = (To be detailed...)`. You are also given an integer array `queries`. The answer to the `j`th query is the size of the smallest interval `i` such that `left_i <= queries[j] <= right_i`. If no such interval exists, the answer is `-1`. Return an array containing the answers to the queries.

## 🛠️ Requirements/Constraints

- $1 \le \text{intervals.length} \le 10^5$
- Intervals are given as $[start, end]$ pairs.

## 🧠 The Engineering Story

**The Villain:** "The Repeated Scan." For every query, scanning all intervals is $O(N \cdot Q)$. We need faster lookups.

**The Hero:** "The Offline Query (Sort + Sweep)." Process queries in order!

**The Plot:**

1. Sort Intervals by start time.
2. Sort Queries (remember original indices to return answers correctly).
3. Iterate through Queries.
4. **Add:** Push all intervals that start before current query into a Min-Heap (ordered by size).
5. **Clean:** Remove intervals from heap that end before current query (they are invalid).
6. **Query:** Top of heap is the smallest valid interval.

**The Twist (Failure):** **Live Queries.** If queries must be online, you need a Segment Tree or Interval Tree. But for static lists, sorting is king.

**Interview Signal:** **Processing Offline Queries** efficiently.

## 🚀 Approach & Intuition
Process sorted queries adding valid intervals to a min-heap.

### C++ Pseudo-Code
```cpp
vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
    sort(intervals.begin(), intervals.end());
    vector<pair<int, int>> sortedQueries;
    for (int i = 0; i < queries.size(); i++) sortedQueries.push_back({queries[i], i});
    sort(sortedQueries.begin(), sortedQueries.end());
    
    vector<int> res(queries.size(), -1);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // {size, end}
    
    int i = 0;
    for (auto& q : sortedQueries) {
        int val = q.first;
        int idx = q.second;
        
        while (i < intervals.size() && intervals[i][0] <= val) {
            int len = intervals[i][1] - intervals[i][0] + 1;
            pq.push({len, intervals[i][1]});
            i++;
        }
        
        while (!pq.empty() && pq.top().second < val) pq.pop();
        
        if (!pq.empty()) res[idx] = pq.top().first;
    }
    return res;
}
```

### Key Observations:

- Sorting intervals by their start or end time is almost always the first step in interval-based problems.
- Use a 'last end time' tracker or a Priority Queue to detect overlaps and manage active intervals.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N + Q \log Q)$
    - **Space Complexity:** $O(N + Q)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the input is sorted or has a limited range? Can you optimize space from $O(N)$ to $O(1)$?
- **Scale Question:** If the dataset is too large to fit in RAM, how would you use external sorting or a distributed hash table?
- **Edge Case Probe:** How does your solution handle duplicates, empty inputs, or extremely large integers?

## 🔗 Related Problems

- [Meeting Rooms II](../meeting_rooms_ii/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
