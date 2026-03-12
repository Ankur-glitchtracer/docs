#  🔗 Graph: Redundant Connection

## 📝 Description
[LeetCode 684](https://leetcode.com/problems/redundant-connection/)
In this problem, a tree is an undirected graph that is connected and has no cycles. You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Cycle Maker." You start with a tree ($N$ nodes, $N-1$ edges). One extra edge is added, creating a cycle. You need to find and remove it.

**The Hero:** "The Union-Find Detective." Iterate through edges. For each edge `(u, v)`:

**The Plot:**

1. Initialize DSU for `N+1` nodes.
2. Iterate `edges`.
3. `if find(u) == find(v)`: Return `[u, v]`.
4. `union(u, v)`.

**The Twist (Failure):** **DFS Alternative.** You can use DFS: For each edge `(u, v)`, check if a path already exists between `u` and `v`. If yes, this edge is redundant. But DFS per edge is $O(N^2)$. DSU is nearly $O(N)$.

**Interview Signal:** Identifying **Cycles via DSU**.

## 🚀 Approach & Intuition
Find the edge that connects two already connected components.

### C++ Pseudo-Code
```cpp
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
        
        for (auto& e : edges) {
            int rootU = find(e[0]);
            int rootV = find(e[1]);
            if (rootU == rootV) return e;
            parent[rootU] = rootV;
        }
        return {};
    }
};
```

### Key Observations:

- Represent the graph using an Adjacency List for space efficiency in sparse graphs.
- Use DFS for path-finding/connectivity and BFS for finding the shortest path in unweighted graphs.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot \alpha(N)) \approx O(N)$.
    - **Space Complexity:** $O(N)$.

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

- [Word Ladder](../word_ladder/PROBLEM.md) — Next in category
- [Connected Components](../number_of_connected_components_in_graph/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
