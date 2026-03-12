#  📡 Advanced Graph: Network Delay Time

## 📝 Description
[LeetCode 743](https://leetcode.com/problems/network-delay-time/)
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target. We will send a signal from a given node `k`. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

## 🛠️ Requirements/Constraints

- $V \le 1000, E \le 10^4$
- Edge weights are non-negative for Dijkstra.

## 🧠 The Engineering Story

**The Villain:** "The Slowest Path." You send a signal from source K. It travels along wires with different latencies. The network is only fully synchronized when the *last* node receives the signal. This is the "longest of shortest paths."

**The Hero:** "Dijkstra's Algorithm." Find the shortest path from K to *all* other nodes. The max of these shortest paths is the answer.

**The Plot:**

1. Build Adjacency List: `u -> {v, w}`.
2. Initialize `dist` map with Infinity, `dist[k] = 0`.
3. Min-Heap `pq`: Push `{0, k}`.
4. While `pq` not empty:
   - Pop `{d, u}`.
   - If `d > dist[u]`, skip (stale).
   - For neighbor `v` with weight `w`:
     - If `d + w < dist[v]`:
       - `dist[v] = d + w`.
       - Push `{dist[v], v}`.
5. Result = `max(dist.values())`. If any node is Infinity, return -1.

**The Twist (Failure):** **Using BFS.** BFS only works for unweighted graphs (or equal weights). With different weights, you *must* use Dijkstra (or Bellman-Ford for negative weights).

**Interview Signal:** Standard **Dijkstra Implementation**.

## 🚀 Approach & Intuition
Shortest path from K to all nodes.

### C++ Pseudo-Code
```cpp
int networkDelayTime(vector<vector<int>>& times, int n, int k) {
    vector<vector<pair<int, int>>> adj(n + 1);
    for (auto& t : times) adj[t[0]].push_back({t[1], t[2]});
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<int> dist(n + 1, INT_MAX);
    
    dist[k] = 0;
    pq.push({0, k});
    
    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;
        
        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    
    int maxDist = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] == INT_MAX) return -1;
        maxDist = max(maxDist, dist[i]);
    }
    return maxDist;
}
```

### Key Observations:

- Dijkstra's and Prim's algorithms use a Priority Queue to find the shortest path or MST in $O(E \log V)$ time.
- Kruskal's algorithm uses Disjoint Set Union (DSU) to efficiently manage connected components and detect cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(E \log V)$
    - **Space Complexity:** $O(V + E)$

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

- [Swim in Rising Water](../swim_in_rising_water/PROBLEM.md) — Next in category
- [Min Cost to Connect Points](../min_cost_to_connect_all_points/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
