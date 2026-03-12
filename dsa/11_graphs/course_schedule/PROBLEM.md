#  🎓 Graph: Course Schedule

## 📝 Description
[LeetCode 207](https://leetcode.com/problems/course-schedule/)
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses. Otherwise, return `false`.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Catch-22." Course A requires B, B requires C, C requires A. You can never graduate. This is a Cycle in a Directed Graph.

**The Hero:** "The Topological Sorter (or Cycle Detector)."

**The Plot:**

1. (To be detailed...)
2. (To be detailed...)

**The Twist (Failure):** **The Disconnected Graph.** A single DFS from node 0 might not visit all nodes. You must iterate `0..N-1` and check every unvisited node.

**Interview Signal:** **Deadlock Detection** / Topological Sort.

## 🚀 Approach & Intuition
0=Unvisited, 1=Visiting, 2=Visited.

### C++ Pseudo-Code
```cpp
class Solution {
    vector<vector<int>> adj;
    vector<int> state; // 0, 1, 2
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        adj.resize(numCourses);
        state.resize(numCourses, 0);
        for (auto& p : prerequisites) adj[p[1]].push_back(p[0]);
        
        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0) {
                if (hasCycle(i)) return false;
            }
        }
        return true;
    }
    
    bool hasCycle(int u) {
        state[u] = 1; // Visiting
        for (int v : adj[u]) {
            if (state[v] == 1) return true;
            if (state[v] == 0) {
                if (hasCycle(v)) return true;
            }
        }
        state[u] = 2; // Visited
        return false;
    }
};
```

### Key Observations:

- Represent the graph using an Adjacency List for space efficiency in sparse graphs.
- Use DFS for path-finding/connectivity and BFS for finding the shortest path in unweighted graphs.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(V + E)$
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

- [Course Schedule II](../course_schedule_ii/PROBLEM.md) — Next in category
- [Surrounded Regions](../surrounded_regions/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
