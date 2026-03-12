#  🔢 Graph: Number of Connected Components in Graph

## 📝 Description
[LeetCode 323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Archipelago." Islands logic again, but this time on a generic graph, not a grid.

**The Hero:** "The Component Counter." Iterate through all nodes. If a node hasn't been visited, it belongs to a new component. Trigger a traversal (DFS/BFS) to mark all its friends.

**The Plot:**

1. Initialize `visited` array and `count = 0`.
2. For `i` from 0 to `n-1`:
   - If `!visited[i]`:
     - `count++`.
     - `DFS(i)` (Mark all reachable nodes).
3. Return `count`.

**The Twist (Failure):** **Union-Find Optimization.** DSU is often cleaner. Start with `N` components. Every successful `union` decrements the count. Return final count.

**Interview Signal:** Basic **Graph Traversal** or **DSU**.

## 🚀 Approach & Intuition
Start with N components, decrement on merge.

### C++ Pseudo-Code
```cpp
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j, int& count) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI != rootJ) {
            parent[rootI] = rootJ;
            count--;
        }
    }
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        int count = n;
        for (auto& e : edges) unite(e[0], e[1], count);
        return count;
    }
};
```

### Key Observations:

- Represent the graph using an Adjacency List for space efficiency in sparse graphs.
- Use DFS for path-finding/connectivity and BFS for finding the shortest path in unweighted graphs.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(V + E)$ (DFS) or $O(E \cdot \alpha(N))$ (DSU).
    - **Space Complexity:** $O(V + E)$.

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

- [Redundant Connection](../redundant_connection/PROBLEM.md) — Next in category
- [Graph Valid Tree](../graph_valid_tree/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
