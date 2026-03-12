#  🌊 Graph: Pacific Atlantic Water Flow

## 📝 Description
[LeetCode 417](https://leetcode.com/problems/pacific-atlantic-water-flow/)
There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the left and top edges of the island, and the Atlantic Ocean touches the right and bottom edges. Rain water flows to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Dual Flow Check." Checking every cell to see if it can flow to Pacific AND Atlantic ($O((MN)^2)$).

**The Hero:** "The Reverse Flow." Water flows downhill. So, from the ocean, water flows *uphill*.

**The Plot:**

1. Create `pacific_reachable` and `atlantic_reachable` sets (boolean grids).
2. Start DFS/BFS from the **Pacific borders** (Top row, Left col) moving only to *equal or higher* cells. Mark `pacific_reachable`.
3. Start DFS/BFS from the **Atlantic borders** (Bottom row, Right col). Mark `atlantic_reachable`.
4. Iterate the grid. If a cell is in BOTH sets, add to result.

**The Twist (Failure):** **The Visited State.** You need distinct visited sets for Pacific and Atlantic traversals.

**Interview Signal:** **Inverse Thinking** (Solving the problem backwards).

## 🚀 Approach & Intuition
Traverse from borders inward (uphill).

### C++ Pseudo-Code
```cpp
class Solution {
    int m, n;
    vector<vector<int>> dirs = {{0,1}, {0,-1}, {1,0}, {-1,0}};
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size(); n = heights[0].size();
        vector<vector<bool>> pac(m, vector<bool>(n, false));
        vector<vector<bool>> atl(m, vector<bool>(n, false));
        
        for (int c = 0; c < n; c++) {
            dfs(heights, 0, c, pac, heights[0][c]);
            dfs(heights, m-1, c, atl, heights[m-1][c]);
        }
        for (int r = 0; r < m; r++) {
            dfs(heights, r, 0, pac, heights[r][0]);
            dfs(heights, r, n-1, atl, heights[r][n-1]);
        }
        
        vector<vector<int>> res;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if (pac[r][c] && atl[r][c]) res.push_back({r, c});
        return res;
    }
    
    void dfs(vector<vector<int>>& grid, int r, int c, vector<vector<bool>>& visit, int prevH) {
        if (r < 0 || c < 0 || r >= m || c >= n || visit[r][c] || grid[r][c] < prevH)
            return;
        visit[r][c] = true;
        for (auto& d : dirs)
            dfs(grid, r+d[0], c+d[1], visit, grid[r][c]);
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

- [Surrounded Regions](../surrounded_regions/PROBLEM.md) — Next in category
- [Rotting Oranges](../rotting_oranges/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
