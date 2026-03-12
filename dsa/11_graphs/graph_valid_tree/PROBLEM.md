#  🌳 Graph: Graph Valid Tree

## 📝 Description
[LeetCode 261](https://leetcode.com/problems/graph-valid-tree/)
Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Imposter Tree." A structure that looks like a tree but has a cycle ($A-B-C-A$) or is disconnected ($A-B, C-D$).

**The Hero:** "The Tree Definition." A graph is a tree if and only if:

**The Plot:**

1. Check Edge Count: If `edges.size() != n - 1`, return `False`.
2. Check Connectivity:
   - Build adjacency list.
   - Run DFS/BFS from node 0.
   - Count visited nodes.
   - Return `visited_count == n`.

**The Twist (Failure):** **Union-Find.** You can also use DSU.

**Interview Signal:** Understanding **Tree Properties** in Graph Theory.

## 🚀 Approach & Intuition
Check loop and single component.

### C++ Pseudo-Code
```cpp
class Solution {
    vector<int> parent;
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int rootI = find(i);
        int rootJ = find(j);
        if (rootI == rootJ) return false; // Cycle
        parent[rootI] = rootJ;
        return true;
    }
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n - 1) return false;
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
        
        int components = n;
        for (auto& e : edges) {
            if (!unite(e[0], e[1])) return false;
            components--;
        }
        return components == 1;
    }
};
```

### Key Observations:

- Represent the graph using an Adjacency List for space efficiency in sparse graphs.
- Use DFS for path-finding/connectivity and BFS for finding the shortest path in unweighted graphs.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
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

- [Connected Components](../number_of_connected_components_in_graph/PROBLEM.md) — Next in category
- [Course Schedule II](../course_schedule_ii/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
