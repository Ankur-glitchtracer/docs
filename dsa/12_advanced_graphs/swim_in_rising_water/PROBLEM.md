#  🏊 Advanced Graph: Swim in Rising Water

## 📝 Description
[LeetCode 778](https://leetcode.com/problems/swim-in-rising-water/)
You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`. The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Return the least time until you can reach the bottom right square `(n - 1, n - 1)` if you start at the top left square `(0, 0)`.

## 🛠️ Requirements/Constraints

- $V \le 1000, E \le 10^4$
- Edge weights are non-negative for Dijkstra.

## 🧠 The Engineering Story

**The Villain:** "The Rising Tide." You can only swim to squares with `elevation <= time`. You want to reach the target at the minimum possible `time`.

**The Hero:** "Modified Dijkstra (or Binary Search on Answer)."

**The Plot:**

1. (To be detailed...)
2. (To be detailed...)

**The Twist (Failure):** **Just checking neighbors.** The "cost" isn't additive like normal Dijkstra. It's a "bottleneck" cost (max edge along path). This is essentially finding the path where the maximum edge weight is minimized.

**Interview Signal:** Dijkstra on **Grid with Bottleneck Capacity**.

## 🚀 Approach & Intuition
Track the max elevation seen so far on the path.

### C++ Pseudo-Code
```cpp
int swimInWater(vector<vector<int>>& grid) {
    int n = grid.size();
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
    vector<vector<bool>> visited(n, vector<bool>(n, false));
    
    pq.push({grid[0][0], 0, 0});
    visited[0][0] = true;
    
    int dirs[] = {0, 1, 0, -1, 0};
    
    while (!pq.empty()) {
        auto [h, r, c] = pq.top(); pq.pop();
        if (r == n - 1 && c == n - 1) return h;
        
        for (int i = 0; i < 4; i++) {
            int nr = r + dirs[i], nc = c + dirs[i+1];
            if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                visited[nr][nc] = true;
                pq.push({max(h, grid[nr][nc]), nr, nc});
            }
        }
    }
    return -1;
}
```

### Key Observations:

- Dijkstra's and Prim's algorithms use a Priority Queue to find the shortest path or MST in $O(E \log V)$ time.
- Kruskal's algorithm uses Disjoint Set Union (DSU) to efficiently manage connected components and detect cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2 \log N)$
    - **Space Complexity:** $O(N^2)$

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

- [Alien Dictionary](../alien_dictionary/PROBLEM.md) — Next in category
- [Network Delay Time](../network_delay_time/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
