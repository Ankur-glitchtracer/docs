#  🎯 Heap: K Closest Points to Origin

## 📝 Description
[LeetCode 973](https://leetcode.com/problems/k-closest-points-to-origin/)
Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`. The distance between two points on the X-Y plane is the Euclidean distance (i.e., $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$).

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The Global Sort." Calculating distance for all $N$ points and sorting them takes $O(N \log N)$. If $N$ is 1 billion and $K$ is 5, we wasted a lot of CPU cycles.

**The Hero:** "The Max-Heap Sieve." Keep a heap of size $K$. Since we want the *smallest* distances, we use a Max-Heap to track the "worst of the best."

**The Plot:**

1. Iterate through points.
2. Calculate squared distance (avoid `sqrt` to keep precision/speed).
3. Push `{dist, point}` to Max-Heap.
4. If heap size > K, pop the max (the furthest point in our current collection).
5. The heap now contains the K closest points.

**The Twist (Failure):** **Min-Heap vs Max-Heap.** Using a Min-Heap requires pushing *all* elements ($O(N \log N)$ total or $O(N)$ with heapify) and then popping K times. A Max-Heap of size K gives $O(N \log K)$, which is faster when $K \ll N$.

**Interview Signal:** Choosing the right heap type for **Top-K** problems.

## 🚀 Approach & Intuition
Maintain the K smallest distances by evicting the largest ones.

### C++ Pseudo-Code
```cpp
vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<pair<int, int>> pq; // {dist, index}
    for (int i = 0; i < points.size(); i++) {
        int dist = points[i][0]*points[i][0] + points[i][1]*points[i][1];
        pq.push({dist, i});
        if (pq.size() > k) pq.pop();
    }
    
    vector<vector<int>> res;
    while (!pq.empty()) {
        res.push_back(points(To be detailed...));
        pq.pop();
    }
    return res;
}
```

### Key Observations:

- Heaps are the go-to for finding the $K$-th largest or smallest element in $O(N \log K)$ time.
- Use a Min-Heap for $K$ largest elements and a Max-Heap for $K$ smallest elements to optimize space.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log K)$
    - **Space Complexity:** $O(K)$

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

- [Kth Largest in Array](../kth_largest_element_in_an_array/PROBLEM.md) — Next in category
- [Last Stone Weight](../last_stone_weight/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Maximum Subarray](../../15_greedy/maximum_subarray/PROBLEM.md) — Prerequisite for Greedy
