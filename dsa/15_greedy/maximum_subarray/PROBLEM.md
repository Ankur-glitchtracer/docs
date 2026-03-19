---
impact: "High"
nr: false
confidence: 5
---
# 📊 Greedy: Maximum Subarray

## 📝 Problem Description
Given an integer array `nums`, find the subarray (containing at least one number) which has the largest sum and return its sum.

!!! info "Real-World Application"
    Used in stock market analysis (Kadane's algorithm), financial data analysis to detect periods of peak profitability, and in signal processing.

## 🛠️ Constraints & Edge Cases
- $1 \le nums.length \le 10^5$
- **Edge Cases:** All negative numbers (should return the largest element).

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    If your current subarray sum becomes negative, it's better to start a new subarray from the next element rather than keeping the negative sum.

### 🐢 Brute Force (Naive)
Calculate sum of every subarray: $O(N^2)$.

### 🐇 Optimal Approach (Kadane's Algorithm)
Iterate through the array. Maintain the `current_sum`. If it drops below zero, reset it. Keep track of the `max_sum`.

### 🧩 Visual Tracing
```mermaid
graph LR
    A[Start] -->|Positive| B[Keep adding]
    B -->|Negative sum| C[Reset]
    C --> D[Restart]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ — One pass through the array.
- **Space Complexity:** $\mathcal{O}(1)$ — Constant space.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Find the subarray sum closest to zero, or return the indices of the subarray.

## 🔗 Related Problems
- [Maximum Product Subarray](../../13_1d_dynamic_programming/maximum_product_subarray/PROBLEM.md)
