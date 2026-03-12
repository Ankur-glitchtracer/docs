#  🔢 Bit Manipulation: Counting Bits

## 📝 Description
[LeetCode 338](https://leetcode.com/problems/counting-bits/)
Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1`'s in the binary representation of `i`.

## 🛠️ Requirements/Constraints

- Inputs are typically 32-bit or 64-bit integers.
- The number of operations is $O(1)$ relative to word size.

## 🧠 The Engineering Story

**The Villain:** "The Repeated Count." Calling `hammingWeight(i)` for every `i` from 0 to `n`. Total $O(N \log N)$ or $O(32N)$.

**The Hero:** "The Pattern DP."

**The Plot:**

1. `dp` array of size `n+1`.
2. `dp[0] = 0`.
3. Iterate `i` from 1 to `n`.
   - `dp[i] = dp[i >> 1] + (i & 1)`.

**The Twist (Failure):** **Offset.** Another pattern is `dp[i] = dp[i & (i-1)] + 1` (Using Kernighan's logic in DP). Both work.

**Interview Signal:** **Bitwise DP**.

## 🚀 Approach & Intuition
`bits[i] = bits[i >> 1] + (i & 1)`.

### C++ Pseudo-Code
```cpp
vector<int> countBits(int n) {
    vector<int> res(n + 1);
    res[0] = 0;
    for (int i = 1; i <= n; i++) {
        res[i] = res[i >> 1] + (i & 1);
    }
    return res;
}
```

### Key Observations:

- Bitwise operations (AND, OR, XOR, NOT) allow for $O(1)$ constant time operations on binary data.
- XOR is particularly useful for finding single elements or toggling states, as $x \oplus x = 0$.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(N)$ (Output array)

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

- [Reverse Bits](../reverse_bits/PROBLEM.md) — Next in category
- [Number of 1 Bits](../number_of_1_bits/PROBLEM.md) — Previous in category
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
