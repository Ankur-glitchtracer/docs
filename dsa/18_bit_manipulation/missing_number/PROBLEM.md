---
impact: "Low"
nr: true
confidence: 5
---
# 🧩 Bit Manipulation: Missing Number

## 📝 Problem Description
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

!!! info "Real-World Application"
    This is used in **detecting missing packets** in networking, identifying missing identifiers in database sequences, or finding gaps in file system allocation tables.

## 🛠️ Constraints & Edge Cases
- `n` = `nums.length`.
- All numbers are unique.
- **Edge Cases:** Array is empty, array missing the first or last number.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    XOR all numbers in the array with all numbers in the range `[0, n]`. The duplicate numbers cancel out (XOR property $A \oplus A = 0$), leaving only the missing one.

### 🐢 Brute Force (Naive)
Sorting the array and checking gaps, or using a Hash Set to track seen numbers. Complexity $\mathcal{O}(N \log N)$ or $\mathcal{O}(N)$ space.

### 🐇 Optimal Approach
Use XOR:
1. `res = 0`.
2. XOR `res` with `i` (index) for all `i`.
3. XOR `res` with `nums[i]` for all `i`.
4. The remaining `res` is the missing number.

### 🧩 Visual Tracing
```mermaid
graph LR
    A[Range 0..n] --> B[Array Elements]
    B -->|XOR| C[Result: Missing Number]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ to iterate.
- **Space Complexity:** $\mathcal{O}(1)$ additional memory.

---

## 🎤 Interview Toolkit

- **Harder Variant:** What if multiple numbers are missing? (Requires frequency map).
- **Alternative Data Structures:** Math formula $Sum(0..N) - Sum(nums)$ works too, but prone to overflow in other languages.

## 🔗 Related Problems
- `[Single Number](#)` — Using XOR property.
- `[Find the Duplicate Number](#)` — Related sequence problem.
