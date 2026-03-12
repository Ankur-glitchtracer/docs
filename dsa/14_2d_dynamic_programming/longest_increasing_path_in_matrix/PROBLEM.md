#  🏔️ DP: Longest Increasing Path in a Matrix

## 📝 Description
[LeetCode 329](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
Given an `m x n` integers `matrix`, return the length of the longest increasing path in `matrix`. From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Graph in Disguise." It's a grid, but moving to larger neighbors forms a Directed Acyclic Graph (DAG). Calculating path length naively involves redundant re-computations.

**The Hero:** "DFS with Memoization."

**The Plot:**

1. `memo[r][c]` stores the longest increasing path starting at `(r, c)`.
2. Iterate every cell. Call `dfs(r, c)`.
3. **DFS(r, c):**
   - If `memo[r][c]` exists, return it.
   - Max length = 1.
   - For each neighbor `(nr, nc)`:
     - If `grid[nr][nc] > grid[r][c]`:
       - `length = max(length, 1 + dfs(nr, nc))`.
   - Store and return length.

**The Twist (Failure):** **Cycles?** No cycles possible because strictly increasing condition prevents revisiting a cell.

**Interview Signal:** **Memoization on Grids**.

## 🚀 Approach & Intuition
Cache results for each cell.

### C++ Pseudo-Code
```cpp
class Solution {
    int m, n;
    vector<vector<int>> memo;
    int dirs[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size(); n = matrix[0].size();
        memo.resize(m, vector<int>(n, 0));
        int maxLen = 0;
        
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                maxLen = max(maxLen, dfs(matrix, r, c));
                
        return maxLen;
    }
    
    int dfs(vector<vector<int>>& mat, int r, int c) {
        if (memo[r][c] != 0) return memo[r][c];
        int len = 1;
        
        for (auto& d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && mat[nr][nc] > mat[r][c]) {
                len = max(len, 1 + dfs(mat, nr, nc));
            }
        }
        return memo[r][c] = len;
    }
};
```

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

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

- **Harder Variant:** Can you optimize the space complexity from $O(N^2)$ to $O(N)$? Can you solve it using a top-down vs bottom-up approach?
- **Scale Question:** If the DP table is too large for memory, can you use 'Check-pointing' or a sliding window of rows to save space?
- **Edge Case Probe:** What are the base cases for empty or single-element inputs? How do you handle negative values if they aren't expected?

## 🔗 Related Problems

- [Distinct Subsequences](../distinct_subsequences/PROBLEM.md) — Next in category
- [Interleaving String](../interleaving_string/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
