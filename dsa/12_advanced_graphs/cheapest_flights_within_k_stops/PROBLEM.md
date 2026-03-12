#  ✈️ Advanced Graph: Cheapest Flights Within K Stops

## 📝 Description
[LeetCode 787](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = (To be detailed...)` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`. You are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

## 🛠️ Requirements/Constraints

- $V \le 1000, E \le 10^4$
- Edge weights are non-negative for Dijkstra.

## 🧠 The Engineering Story

**The Villain:** "The Infinite Path." Dijkstra finds the shortest path by cost, but it might take 100 stops. We are constrained to `K` stops. A cheaper path might be invalid if it's too long.

**The Hero:** "Bellman-Ford (or BFS with Levels)." We iterate exactly `K+1` times.

**The Plot:**

1. (To be detailed...)
2. (To be detailed...)

**The Twist (Failure):** **Using Dijkstra blindly.** Dijkstra greedily expands the cheapest path. The cheapest path might use 5 stops. When we reject it, we might never find the slightly more expensive path that uses 2 stops unless we track `(cost, stops)` as the state in the priority queue.

**Interview Signal:** Constrained Shortest Path (**Bellman-Ford variant**).

## 🚀 Approach & Intuition
Relax edges K+1 times.

### C++ Pseudo-Code
```cpp
int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
    vector<int> prices(n, INT_MAX);
    prices[src] = 0;
    
    for (int i = 0; i <= k; i++) {
        vector<int> temp = prices;
        for (auto& f : flights) {
            int u = f[0], v = f[1], w = f[2];
            if (prices[u] != INT_MAX) {
                temp[v] = min(temp[v], prices[u] + w);
            }
        }
        prices = temp;
    }
    return prices[dst] == INT_MAX ? -1 : prices[dst];
}
```

### Key Observations:

- Dijkstra's and Prim's algorithms use a Priority Queue to find the shortest path or MST in $O(E \log V)$ time.
- Kruskal's algorithm uses Disjoint Set Union (DSU) to efficiently manage connected components and detect cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(K \cdot E)$
    - **Space Complexity:** $O(N)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you solve this using BFS for shortest paths or DFS for connectivity? When would you use Union-Find?
- **Scale Question:** If the graph has billions of edges (like a social network), how would you use a Pregel or Giraph-style distributed processing model?
- **Edge Case Probe:** How do you handle cycles, disconnected components, or self-loops in the graph?

## 🔗 Related Problems

- [Alien Dictionary](../alien_dictionary/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
