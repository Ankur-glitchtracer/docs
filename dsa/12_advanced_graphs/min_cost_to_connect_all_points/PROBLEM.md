#  🔌 Advanced Graph: Min Cost to Connect All Points

## 📝 Description
[LeetCode 1584](https://leetcode.com/problems/min-cost-to-connect-all-points/)
You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`. The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance between them: `|xi - xj| + |yi - yj|`. Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

## 🛠️ Requirements/Constraints

- $V \le 1000, E \le 10^4$
- Edge weights are non-negative for Dijkstra.

## 🧠 The Engineering Story

**The Villain:** "The Cable Bill." You need to connect N servers with cables. Connecting every pair ($N^2$ cables) is expensive. You want the Minimum Spanning Tree (MST).

**The Hero:** "Prim's Algorithm." Start from one node and greedily attach the closest unvisited node.

**The Plot:**

1. Start at point
0. `cost = 0`. `visited = {0}`.
2. Maintain a Min-Heap of edges `{dist, node}` from the *visited* set to the *unvisited* world.
3. Initially push all edges from point 0.
4. While `visited.size() < N`:
   - Pop smallest edge `{d, u}`.
   - If `u` visited, skip.
   - Else:
     - Mark `u` visited.
     - `cost += d`.
     - Push all edges from `u` to unvisited nodes.

**The Twist (Failure):** **Kruskal's vs Prim's.** Kruskal's (sort edges + Union-Find) works well too ($O(E \log E)$). Since this is a dense graph ($E \approx V^2$), Prim's is often preferred or equal.

**Interview Signal:** Implementing **MST (Minimum Spanning Tree)**.

## 🚀 Approach & Intuition
Greedily pick shortest edge from visited to unvisited.

### C++ Pseudo-Code
```cpp
int minCostConnectPoints(vector<vector<int>>& points) {
    int n = points.size();
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<bool> visited(n, false);
    
    pq.push({0, 0}); // {cost, node}
    int res = 0, connected = 0;
    
    while (connected < n) {
        auto [cost, u] = pq.top(); pq.pop();
        if (visited[u]) continue;
        
        visited[u] = true;
        res += cost;
        connected++;
        
        for (int v = 0; v < n; v++) {
            if (!visited[v]) {
                int dist = abs(points[u][0] - points[v][0]) + 
                           abs(points[u][1] - points[v][1]);
                pq.push({dist, v});
            }
        }
    }
    return res;
}
```

### Key Observations:

- Dijkstra's and Prim's algorithms use a Priority Queue to find the shortest path or MST in $O(E \log V)$ time.
- Kruskal's algorithm uses Disjoint Set Union (DSU) to efficiently manage connected components and detect cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2 \log N)$ (Prim's) or $O(N^2)$ (Optimized Prim's)
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

- [Network Delay Time](../network_delay_time/PROBLEM.md) — Next in category
- [Reconstruct Itinerary](../reconstruct_itinerary/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
