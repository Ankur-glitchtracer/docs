#  🔎 Backtracking: Word Search

## 📝 Description
[LeetCode 79](https://leetcode.com/problems/word-search/)
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Wandering Path." Finding a word in a 2D grid where you can turn left, right, up, or down. The path cannot cross itself.

**The Hero:** "The DFS with Visitation."

**The Plot:**

1. Iterate through every cell `(r, c)`.
2. If `grid[r][c]` matches the first letter, launch a DFS.
3. **DFS Logic:**
   - Base Case: `index == word.length` -> Found!
   - Boundary Check: Out of bounds or mismatch -> Return False.
   - Cycle Check: If cell is visited -> Return False.
   - **Mark Visited:** Temporarily mark `grid[r][c]` (e.g., with '#').
   - Recurse in 4 directions.
   - **Backtrack:** Restore `grid[r][c]` to original value.
   - Return `OR` of all directions.

**The Twist (Failure):** **Creating a new Visited Set.** Passing a `visited` set by value in recursion is too slow ($O(N^2)$ copy cost). Modifying the grid in-place is $O(1)$ space and much faster.

**Interview Signal:** In-place **Grid Modification** for state tracking.

## 🚀 Approach & Intuition
Search from every cell matching the first character.

### C++ Pseudo-Code
```cpp
bool exist(vector<vector<char>>& board, string word) {
    int m = board.size(), n = board[0].size();
    
    function<bool(int, int, int)> dfs = [&](int r, int c, int i) {
        if (i == word.size()) return true;
        if (r < 0 || c < 0 || r >= m || c >= n || board[r][c] != word[i]) return false;
        
        char temp = board[r][c];
        board[r][c] = '#'; // Mark visited
        
        bool res = dfs(r+1, c, i+1) || dfs(r-1, c, i+1) || 
                   dfs(r, c+1, i+1) || dfs(r, c-1, i+1);
                   
        board[r][c] = temp; // Backtrack
        return res;
    };
    
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (dfs(r, c, 0)) return true;
        }
    }
    return false;
}
```

### Key Observations:

- Backtracking is essentially a DFS on a state-space tree where we 'undo' the last move to explore other branches.
- Pruning is the most important optimization to skip branches that cannot lead to a valid solution.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot M \cdot 4^L)$ where L is word length.
    - **Space Complexity:** $O(L)$ (Recursion depth)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you use Pruning or Bitmasking to significantly reduce the search space?
- **Scale Question:** How would you parallelize the search? Would you use Work Stealing to balance the load between threads?
- **Edge Case Probe:** What is the maximum depth of recursion before you hit a stack overflow?

## 🔗 Related Problems

- [Palindrome Partitioning](../palindrome_partitioning/PROBLEM.md) — Next in category
- [Combination Sum II](../combination_sum_ii/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
