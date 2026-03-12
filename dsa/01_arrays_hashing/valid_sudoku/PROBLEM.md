#  🔢 Arrays & Hashing: Valid Sudoku

## 📝 Description
[LeetCode 36](https://leetcode.com/problems/valid-sudoku/)
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes must contain the digits `1-9` without repetition.

## 🛠️ Requirements/Constraints

- $board.length == 9$
- $board[i].length == 9$
- $board[i][j]$ is a digit 1-9 or '.'

## 🧠 The Engineering Story

**The Villain:** "The Complex Indexer." Trying to verify 3x3 sub-grids using nasty nested loops and confusing modulo arithmetic (`(r // 3) * 3 + c // 3`). Off-by-one errors abound.

**The Hero:** "The Hash Set Trio." Simply maintain sets for Rows, Columns, and Boxes.

**The Plot:**

1. Initialize sets (or boolean arrays) for `rows[9]`, `cols[9]`, and `boxes[3][3]`.
2. Iterate through the entire board.
3. If cell is not empty:
   - Check if the number exists in the corresponding Row Set, Col Set, or Box Set.
   - If yes -> Invalid.
   - If no -> Add to all three sets.

**The Twist (Failure):** **The Box Mapping.** Understanding that the box index for a cell at `(r, c)` is simply `(r / 3, c / 3)`.

**Interview Signal:** Ability to simplify **2D Grid Logic** using sets.

## 🚀 Approach & Intuition
Use sets to track seen numbers for rows, columns, and 3x3 boxes.

### C++ Pseudo-Code
```cpp
bool isValidSudoku(vector<vector<char>>& board) {
    int rows[9][9] = {0}, cols[9][9] = {0}, boxes[3][3][9] = {0};
    
    for (int r = 0; r < 9; r++) {
        for (int c = 0; c < 9; c++) {
            if (board[r][c] == '.') continue;
            int num = board[r][c] - '1'; // 0-8 index
            
            if (rows[r][num] || cols[c][num] || boxes[r/3][c/3][num])
                return false;
                
            rows[r][num] = cols[c][num] = boxes[r/3][c/3][num] = 1;
        }
    }
    return true;
}
```

### Key Observations:

- We only need to validate the filled cells; empty cells can be ignored.
- Using bitmasks or a set of strings like 'row_i_val', 'col_j_val', 'box_k_val' can simplify the validation logic.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(1)$ (Grid size is fixed at 9x9)
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Could you write a solver that fills in the empty cells (Sudoku Solver using Backtracking)?
- **Scale Question:** How would you validate a $N^2 \times N^2$ Sudoku board efficiently?
- **Edge Case Probe:** What if the board is partially filled but contains invalid characters instead of just digits and dots?

## 🔗 Related Problems

- [Encode and Decode Strings](../encode_and_decode_strings/PROBLEM.md) — Next in category
- [Product of Array Except Self](../product_of_array_except_self/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
