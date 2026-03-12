#  🎓 Graph: Course Schedule II

## 📝 Description
[LeetCode 210](https://leetcode.com/problems/course-schedule-ii/)
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Order Demand." Not only must we detect cycles, but we must also output the valid order.

**The Hero:** "Kahn's Algorithm (BFS) or Post-Order DFS."

**The Plot:**

1. (To be detailed...)
2. (To be detailed...)

**The Twist (Failure):** **DFS Output.** If using DFS, the topological sort is the *reverse* of the Post-Order completion. Add to list at the end of recursion, then reverse the list.

**Interview Signal:** Implementing **Topological Sort**.

## 🚀 Approach & Intuition
Process nodes with 0 dependencies.

### C++ Pseudo-Code
```cpp
vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> adj(numCourses);
    vector<int> indegree(numCourses, 0);
    for (auto& p : prerequisites) {
        adj[p[1]].push_back(p[0]);
        indegree[p[0]]++;
    }
    
    queue<int> q;
    for (int i = 0; i < numCourses; i++)
        if (indegree[i] == 0) q.push(i);
        
    vector<int> res;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        res.push_back(u);
        for (int v : adj[u]) {
            indegree[v]--;
            if (indegree[v] == 0) q.push(v);
        }
    }
    
    return res.size() == numCourses ? res : vector<int>{};
}
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

- [Graph Valid Tree](../graph_valid_tree/PROBLEM.md) — Next in category
- [Course Schedule](../course_schedule/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
