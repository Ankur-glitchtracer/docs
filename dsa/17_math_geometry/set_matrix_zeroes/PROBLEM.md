#  0️⃣ Math: Set Matrix Zeroes

## 📝 Description
[LeetCode 73](https://leetcode.com/problems/set-matrix-zeroes/)
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s. You must do it in place.

## 🛠️ Requirements/Constraints

- Numerical values fit within standard data types (int, long).
- Coordinate ranges are typically within $10^4$.

## 🧠 The Engineering Story

**The Villain:** "The Cascading Zero." If you iterate and set rows/cols to zero immediately, those new zeros will cause *other* rows/cols to become zero in future steps. The whole matrix becomes zero.

**The Hero:** "The State Marker." We need to mark rows/cols for deletion without destroying the data we haven't processed yet.

**The Plot:**

1. Use the **first row** and **first column** as markers.
2. If `matrix[i][j] == 0`: set `matrix[i][0] = 0` and `matrix[0][j] = 0`.
3. Handle `matrix[0][0]` ambiguity (overlap of row 0 and col 0) with a separate flag `row0_zero`.
4. Iterate inner matrix (`1..m`, `1..n`): if row/col marker is 0, set cell to 0.
5. Handle first row and first column separately based on flags.

**The Twist (Failure):** **Processing Order.** You must process the inner matrix first, using the markers. *Then* process the markers themselves. If you zero out the markers first, you lose the data needed for the inner matrix.

**Interview Signal:** **In-place Space Optimization** ($O(1)$ space).

## 🚀 Approach & Intuition
Use the matrix itself to store state.

### C++ Pseudo-Code
```cpp
void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size(), n = matrix[0].size();
    bool firstRow = false, firstCol = false;
    
    for (int i = 0; i < m; i++) 
        if (matrix[i][0] == 0) firstCol = true;
        
    for (int j = 0; j < n; j++) 
        if (matrix[0][j] == 0) firstRow = true;
        
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0)
                matrix[i][j] = 0;
        }
    }
    
    if (firstCol) for (int i = 0; i < m; i++) matrix[i][0] = 0;
    if (firstRow) for (int j = 0; j < n; j++) matrix[0][j] = 0;
}
```

### Key Observations:

- Use modular arithmetic to prevent integer overflow and the Euclidean algorithm for GCD/LCM problems.
- In geometry, use cross products to determine orientation and the distance formula for proximity checks.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
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

- [Happy Number](../happy_number/PROBLEM.md) — Next in category
- [Spiral Matrix](../spiral_matrix/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite: Bit Manipulation
