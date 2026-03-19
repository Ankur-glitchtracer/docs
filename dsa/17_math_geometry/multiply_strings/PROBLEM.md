---
impact: "High"
nr: false
confidence: 4
---
# 🟦 Math & Geometry: Multiply Strings

## 📝 Problem Description
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string. You must not use any built-in BigInteger libraries.

!!! info "Real-World Application"
    Fundamental in implementing **arbitrary-precision arithmetic** in calculators, cryptographic libraries, and scientific software that handles numbers exceeding CPU-native bit sizes.

## 🛠️ Constraints & Edge Cases
- `num1`, `num2` can be very large strings (up to 200 digits).
- **Edge Cases:** "0", trailing zeros.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    The product of two numbers with lengths $M$ and $N$ will have a length of at most $M+N$. We can use an array of size $M+N$ to store intermediate digit products, starting from the last index.

### 🐢 Brute Force (Naive)
Convert strings to integers, multiply, and convert back. This fails for very large numbers because they exceed standard integer type limits.

### 🐇 Optimal Approach
1. Initialize an array of size $M+N$ with zeros.
2. Iterate backwards through both strings.
3. Multiply each digit: `prod = (num1[i] - '0') * (num2[j] - '0')`.
4. Add to the product index `i + j + 1`, and update the carry at `i + j`.
5. Finally, convert the array to a string, skipping leading zeros.

### 🧩 Visual Tracing
```mermaid
graph LR
    A[num1: '12'] -->|x| B[num2: '34']
    B --> C{pos[i+j] + carry}
    C --> D[Result: '408']
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(M \times N)$ where $M, N$ are string lengths. We nested-loop the digits.
- **Space Complexity:** $\mathcal{O}(M + N)$ to store the result array.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Implement addition of two big integers represented as strings.
- **Alternative Data Structures:** Using list of integers vs array.

## 🔗 Related Problems
- `[Plus One](#)` — Basic big integer arithmetic simulation.
- `[Sum of Two Integers](#)` — Bitwise arithmetic.
