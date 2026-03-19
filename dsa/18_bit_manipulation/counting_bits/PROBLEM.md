---
impact: "Low"
nr: true
confidence: 5
---
# 🧩 Bit Manipulation: Counting Bits

## 📝 Problem Description
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i`, `ans[i]` is the number of `1` bits in the binary representation of `i`.

!!! info "Real-World Application"
    Essential for **performance-sensitive optimization** tasks, such as calculating Hamming weight for checksums, error detection, or data compression algorithms (e.g., LZ77) where counting bits is a frequent operation.

## 🛠️ Constraints & Edge Cases
- $0 \le n \le 10^5$
- **Edge Cases:** $n=0$.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Use dynamic programming: For any number `i`, the number of bits is `bits[i >> 1] + (i & 1)`. This reuses computed results from the previous sub-problems.

### 🐢 Brute Force (Naive)
Iterate from 0 to $n$ and count bits for each using `n & (n-1)` or built-in functions. Complexity $\mathcal{O}(N \log N)$.

### 🐇 Optimal Approach
Use DP:
- `ans[i] = ans[i >> 1] + (i % 2)`.
- This works because shifting right removes the last bit, and the remainder tells us if the last bit was 1.

### 🧩 Visual Tracing
```mermaid
graph LR
    A[i: 5 binary 101] --> B[i>>1: 2 binary 10]
    B --> C[ans[i] = ans[2] + 1]
    C --> D[Result: 2]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ where $N$ is the input integer.
- **Space Complexity:** $\mathcal{O}(N)$ to store the array of bit counts.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Use $\mathcal{O}(1)$ additional space (impossible here as we return an array).
- **Alternative Data Structures:** Bit shifting vs. arithmetic.

## 🔗 Related Problems
- `[Number of 1 Bits](#)` — Single number bit counting.
- `[Single Number](#)` — Using XOR.
