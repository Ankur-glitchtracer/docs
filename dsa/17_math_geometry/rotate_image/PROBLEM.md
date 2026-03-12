#  🔄 Math: Rotate Image

## 📝 Description
[LeetCode 48](https://leetcode.com/problems/rotate-image/)
You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise). You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

## 🛠️ Requirements/Constraints

- Numerical values fit within standard data types (int, long).
- Coordinate ranges are typically within $10^4$.

## 🧠 The Engineering Story

**The Villain:** "The In-Place Rotation." Rotating a 2D matrix by 90 degrees requires moving elements in cycles. If you use a new matrix, it's easy ($O(N^2)$ space). Doing it in-place without overwriting data you still need is the challenge.

**The Hero:** "The Transpose + Reflect."

**The Plot:**

1. **Transpose:** Swap `matrix[i][j]` with `matrix[j][i]`. (Reflect across main diagonal).
2. **Reflect:** Reverse every row.
3. Result is a 90-degree clockwise rotation.

**The Twist (Failure):** **Anti-clockwise.** For counter-clockwise, Transpose then Reverse Columns (instead of rows).

**Interview Signal:** **Linear Algebra** transformations.

## 🚀 Approach & Intuition
Swap across diagonal, then reverse rows.

### C++ Pseudo-Code
```cpp
void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();
    
    // Transpose
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    
    // Reverse rows
    for (int i = 0; i < n; i++) {
        reverse(matrix[i].begin(), matrix[i].end());
    }
}
```

### Key Observations:

- Use modular arithmetic to prevent integer overflow and the Euclidean algorithm for GCD/LCM problems.
- In geometry, use cross products to determine orientation and the distance formula for proximity checks.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2)$
    - **Space Complexity:** $O(1)$

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

- [Spiral Matrix](../spiral_matrix/PROBLEM.md) — Next in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite: Bit Manipulation
