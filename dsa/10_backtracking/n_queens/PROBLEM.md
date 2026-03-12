#  👑 Backtracking: N-Queens

## 📝 Description
[LeetCode 51](https://leetcode.com/problems/n-queens/)
The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Return all distinct solutions to the n-queens puzzle.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Diagonal Threat." Placing `N` queens on an `NxN` board so no two attack each other. Checking diagonals efficiently is the hard part.

**The Hero:** "The Set Tracker." Use 3 Sets (or boolean arrays) to track occupied lines:

**The Plot:**

1. Iterate `row` from 0 to N.
2. For each `col` in 0 to N:
   - Check if `col`, `r+c`, or `r-c` is in sets.
   - If valid: Add Queen. Update Sets. Recurse `row + 1`.
   - Backtrack: Remove Queen. Revert Sets.

**The Twist (Failure):** **String Construction.** Building the board representation (`(To be detailed...)`) at the very end is faster than maintaining a grid of strings throughout recursion.

**Interview Signal:** Optimizing **Constraint Checking** with math.

## 🚀 Approach & Intuition
Track columns and diagonals to place queens safely.

### C++ Pseudo-Code
```cpp
vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> res;
    vector<string> board(n, string(n, '.'));
    unordered_set<int> cols, posDiag, negDiag;
    
    function<void(int)> backtrack = [&](int r) {
        if (r == n) {
            res.push_back(board);
            return;
        }
        for (int c = 0; c < n; c++) {
            if (cols.count(c) || posDiag.count(r + c) || negDiag.count(r - c))
                continue;
                
            cols.insert(c);
            posDiag.insert(r + c);
            negDiag.insert(r - c);
            board[r][c] = 'Q';
            
            backtrack(r + 1);
            
            cols.erase(c);
            posDiag.erase(r + c);
            negDiag.erase(r - c);
            board[r][c] = '.';
        }
    };
    
    backtrack(0);
    return res;
}
```

### Key Observations:

- Backtracking is essentially a DFS on a state-space tree where we 'undo' the last move to explore other branches.
- Pruning is the most important optimization to skip branches that cannot lead to a valid solution.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N!)$
    - **Space Complexity:** $O(N)$

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

- [Letter Combinations](../letter_combinations_of_a_phone_number/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite: Trees
