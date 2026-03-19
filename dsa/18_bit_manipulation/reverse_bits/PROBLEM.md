---
impact: "Low"
nr: true
confidence: 4
---
# 🧩 Bit Manipulation: Reverse Bits

## 📝 Problem Description
Reverse bits of a given 32-bit unsigned integer.

!!! info "Real-World Application"
    Critical in **network protocol parsing** (e.g., bit-endianness swap between big-endian and little-endian systems), digital signal processing, and low-level communication drivers.

## 🛠️ Constraints & Edge Cases
- 32-bit input.
- **Edge Cases:** All zeros, all ones.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Iterate 32 times. In each step, extract the last bit of the source (`n & 1`) and shift it into the result (`res = (res << 1) + bit`).

### 🐢 Brute Force (Naive)
Convert to string, reverse string, convert back to integer. $\mathcal{O}(N)$ but inefficient.

### 🐇 Optimal Approach
1. Initialize `res = 0`.
2. Loop 32 times:
    - `res = (res << 1) | (n & 1)`
    - `n >>= 1`
3. Return `res`.

### 🧩 Visual Tracing
```mermaid
graph LR
    A[Source] -->|Pop Bit| B[Res]
    B -->|Push Bit| C[Shifted Res]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(1)$ (fixed 32 iterations).
- **Space Complexity:** $\mathcal{O}(1)$.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Use Divide & Conquer (swap bit chunks: 16-bit, then 8-bit, etc.).
- **Alternative Data Structures:** Lookup tables for 8-bit chunks.

## 🔗 Related Problems
- `[Number of 1 Bits](#)` — Counting bits.
- `[Reverse Integer](#)` — Reversing digits.
