#  🏝️ Graph: Max Area of Island

## 📝 Description
[LeetCode 695](https://leetcode.com/problems/max-area-of-island/)
You are given an `m x n` binary matrix `grid`. An island is a group of `1`s (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water. The area of an island is the number of cells with a value `1` in the island. Return the maximum area of an island in `grid`. If there is no island, return `0`.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Counting Confusion." Similar to Number of Islands, but now we need the *size* of the biggest one. Just passing a counter globally can be messy with recursion.

**The Hero:** "The Accumulator DFS." The DFS function shouldn't just return void; it should return the size of the island chunk it just visited. `1 + dfs(up) + dfs(down)...`.

**The Plot:**

1. Iterate grid. If '1', start DFS.
2. **DFS:**
   - Mark visited (set to '0').
   - `size = 1`.
   - `size += dfs(neighbors)`.
   - Return `size`.
3. Track `max_size`.

**The Twist (Failure):** **Stack Depth.** For a $50 \times 50$ grid of all 1s, recursion depth is 2500. This is fine, but for larger grids, Iterative DFS or BFS prevents Stack Overflow.

**Interview Signal:** Modifying traversal to **Aggregate Values**.

## 🚀 Approach & Intuition
Return sum of 1 + neighbors.

### C++ Pseudo-Code
```cpp
class Solution {
    int m, n;
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        m = grid.size(); n = grid[0].size();
        int maxArea = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    maxArea = max(maxArea, dfs(grid, r, c));
                }
            }
        }
        return maxArea;
    }
    
    int dfs(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || c < 0 || r >= m || c >= n || grid[r][c] == 0) return 0;
        grid[r][c] = 0; // Visit
        return 1 + dfs(grid, r+1, c) + dfs(grid, r-1, c) + 
                   dfs(grid, r, c+1) + dfs(grid, r, c-1);
    }
};
```

### Key Observations:

- Represent the graph using an Adjacency List for space efficiency in sparse graphs.
- Use DFS for path-finding/connectivity and BFS for finding the shortest path in unweighted graphs.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
    - **Space Complexity:** $O(M 	imes N)$

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

- [Clone Graph](../clone_graph/PROBLEM.md) — Next in category
- [Number of Islands](../number_of_islands/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
