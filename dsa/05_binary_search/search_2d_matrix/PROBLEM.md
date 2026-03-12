#  📉 Binary Search: Search a 2D Matrix

## 📝 Description
[LeetCode 74](https://leetcode.com/problems/search-a-2d-matrix/)
Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Target value is within the range of the data type.

## 🧠 The Engineering Story

**The Villain:** "The Double Search." Searching the row first, then the column. Or worse, treating it as a grid and doing $O(M+N)$ scanning.

**The Hero:** "The Virtual Flattener." Treating the 2D matrix as a single 1D sorted array of size $M \times N$.

**The Plot:**

1. `low = 0`, `high = (m * n) - 1`.
2. Map `mid` index to 2D coordinates:
   - `row = mid // cols`
   - `col = mid % cols`
3. Perform standard binary search using `matrix[row][col]`.

**The Twist (Failure):** **The Empty Matrix.** Input `[]` or `[[]]` can cause division by zero or index errors if not handled.

**Interview Signal:** Coordinate mapping and logical simplification.

## 🚀 Approach & Intuition
Treat the matrix as a sorted list.

### C++ Pseudo-Code
```cpp
bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) return false;
    int m = matrix.size(), n = matrix[0].size();
    int l = 0, r = m * n - 1;
    
    while (l <= r) {
        int mid = l + (r - l) / 2;
        int val = matrix[mid / n][mid % n];
        if (val == target) return true;
        if (val < target) l = mid + 1;
        else r = mid - 1;
    }
    return false;
}
```

### Key Observations:

- Binary search can be applied not just to sorted arrays, but to any monotonic search space (Search on Answer).
- Be careful with the boundaries ($left, right$) and the condition for moving them to avoid infinite loops.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log(M \times N))$
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you apply 'Binary Search on Answer' to solve optimization problems (e.g., minimize max distance)?
- **Scale Question:** If you are searching in a distributed database, how can you reduce the number of network round trips?
- **Edge Case Probe:** Does your mid-point calculation `(left + right) / 2` overflow for very large indices?

## 🔗 Related Problems

- [Koko Eating Bananas](../koko_eating_bananas/PROBLEM.md) — Next in category
- [Binary Search](../binary_search/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
