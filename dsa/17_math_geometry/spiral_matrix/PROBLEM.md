#  🌀 Math: Spiral Matrix

## 📝 Description
[LeetCode 54](https://leetcode.com/problems/spiral-matrix/)
Given an `m x n` matrix, return all elements of the matrix in spiral order.

## 🛠️ Requirements/Constraints

- Numerical values fit within standard data types (int, long).
- Coordinate ranges are typically within $10^4$.

## 🧠 The Engineering Story

**The Villain:** "The Index Dance." Simulating a spiral walk involves managing boundaries (`top`, `bottom`, `left`, `right`) and ensuring you don't overshoot or revisit cells.

**The Hero:** "The Layer Peeler." Treat the matrix as a set of concentric rectangles.

**The Plot:**

1. Initialize boundaries: `top=0`, `bottom=m-1`, `left=0`, `right=n-1`.
2. While `top <= bottom` and `left <= right`:
   - Traverse **Right**: `(top, left)` to `(top, right)`. `top++`.
   - Traverse **Down**: `(top, right)` to `(bottom, right)`. `right--`.
   - If valid: Traverse **Left**: `(bottom, right)` to `(bottom, left)`. `bottom--`.
   - If valid: Traverse **Up**: `(bottom, left)` to `(top, left)`. `left++`.

**The Twist (Failure):** **The Center Line.** If the matrix is a single row or column, the loop might double-count the last leg (Left or Up) if you don't check `top <= bottom` and `left <= right` again inside the loop.

**Interview Signal:** **Simulation** and boundary management.

## 🚀 Approach & Intuition
Shrink bounds after every pass.

### C++ Pseudo-Code
```cpp
vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> res;
    int top = 0, bottom = matrix.size() - 1;
    int left = 0, right = matrix[0].size() - 1;
    
    while (top <= bottom && left <= right) {
        for (int i = left; i <= right; i++) res.push_back(matrix[top][i]);
        top++;
        
        for (int i = top; i <= bottom; i++) res.push_back(matrix[i][right]);
        right--;
        
        if (top <= bottom) {
            for (int i = right; i >= left; i--) res.push_back(matrix[bottom][i]);
            bottom--;
        }
        
        if (left <= right) {
            for (int i = bottom; i >= top; i--) res.push_back(matrix[i][left]);
            left++;
        }
    }
    return res;
}
```

### Key Observations:

- Use modular arithmetic to prevent integer overflow and the Euclidean algorithm for GCD/LCM problems.
- In geometry, use cross products to determine orientation and the distance formula for proximity checks.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
    - **Space Complexity:** $O(1)$ (Excluding output)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you solve this without using any arithmetic operators (+, -, *, /)?
- **Scale Question:** How do you handle bit operations on arbitrarily large integers (BigInt)?
- **Edge Case Probe:** How does your code handle signed vs unsigned integers and overflow/underflow?

## 🔗 Related Problems

- [Set Matrix Zeroes](../set_matrix_zeroes/PROBLEM.md) — Next in category
- [Rotate Image](../rotate_image/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite: Bit Manipulation
