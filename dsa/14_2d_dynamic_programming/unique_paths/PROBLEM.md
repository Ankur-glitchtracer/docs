#  🤖 DP: Unique Paths

## 📝 Description
[LeetCode 62](https://leetcode.com/problems/unique-paths/)
There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time. Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Maze of Many Paths." Counting all possible paths from Top-Left to Bottom-Right. Recursion is $O(2^{M+N})$.

**The Hero:** "The Grid Accumulator." The number of ways to reach cell `(i, j)` is simply `ways(i-1, j) + ways(i, j-1)` (from top + from left).

**The Plot:**

1. Create `dp` table or simply use a 1D array (row).
2. Initialize first row to 1s.
3. For each subsequent row:
   - `new_row[0] = 1`.
   - `new_row[j] = new_row[j-1] (left) + old_row[j] (top)`.
4. Return last element.

**The Twist (Failure):** **Integer Overflow.** For very large grids, the number of paths exceeds 32-bit int. (LeetCode constraints are usually small enough).

**Interview Signal:** Basic **2D Grid DP**.

## 🚀 Approach & Intuition
Accumulate paths from top and left.

### C++ Pseudo-Code
```cpp
int uniquePaths(int m, int n) {
    vector<int> row(n, 1);
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            row[j] += row[j-1];
        }
    }
    return row[n-1];
}
```

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
    - **Space Complexity:** $O(N)$ (Row optimized) or $O(1)$ (Math combinations)

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

- [Longest Common Subsequence](../longest_common_subsequence/PROBLEM.md) — Next in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
