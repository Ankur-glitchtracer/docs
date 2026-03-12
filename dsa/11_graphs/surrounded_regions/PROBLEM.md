#  ❌ Graph: Surrounded Regions

## 📝 Description
[LeetCode 130](https://leetcode.com/problems/surrounded-regions/)
Given an `m x n` matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded region.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The False Capture." You see a '0' and want to flip it to 'X'. But wait! What if it's connected to a '0' that touches the border? Then it's not surrounded.

**The Hero:** "The Border Patrol." Any '0' connected to the border *cannot* be captured. Everything else can.

**The Plot:**

1. Scan the **borders** (rows 0/m-1, cols 0/n-1).
2. If you find a '0', run DFS/BFS to mark it and all its connected '0's as "Safe" (e.g., change '0' to '#').
3. Iterate the entire grid.
   - If '0': It wasn't marked Safe. Capture it (flip to 'X').
   - If '#': It was Safe. Restore it (flip back to '0').

**The Twist (Failure):** **Internal Cycles.** '0's might form a loop inside. This doesn't matter; if they don't touch the border, the whole loop is captured.

**Interview Signal:** **Boundary Traversal** logic.

## 🚀 Approach & Intuition
Mark border-connected 'O's first.

### C++ Pseudo-Code
```cpp
class Solution {
    int m, n;
public:
    void solve(vector<vector<char>>& board) {
        m = board.size(); n = board[0].size();
        // 1. Mark border-connected 'O's as '#'
        for (int r = 0; r < m; r++) {
            dfs(board, r, 0);
            dfs(board, r, n-1);
        }
        for (int c = 0; c < n; c++) {
            dfs(board, 0, c);
            dfs(board, m-1, c);
        }
        // 2. Flip remaining 'O'->'X', '#'->'O'
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (board[r][c] == 'O') board[r][c] = 'X';
                if (board[r][c] == '#') board[r][c] = 'O';
            }
        }
    }
    
    void dfs(vector<vector<char>>& board, int r, int c) {
        if (r < 0 || c < 0 || r >= m || c >= n || board[r][c] != 'O') return;
        board[r][c] = '#';
        dfs(board, r+1, c); dfs(board, r-1, c);
        dfs(board, r, c+1); dfs(board, r, c-1);
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

- [Course Schedule](../course_schedule/PROBLEM.md) — Next in category
- [Pacific Atlantic Water Flow](../pacific_atlantic_water_flow/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
