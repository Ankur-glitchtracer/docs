#  🔄 Bit Manipulation: Reverse Bits

## 📝 Description
[LeetCode 190](https://leetcode.com/problems/reverse-bits/)
Reverse bits of a given 32-bit unsigned integer.

## 🛠️ Requirements/Constraints

- Inputs are typically 32-bit or 64-bit integers.
- The number of operations is $O(1)$ relative to word size.

## 🧠 The Engineering Story

**The Villain:** "The Array Converter." Converting int to `bool[32]`, reversing array, converting back. Slow and heavy.

**The Hero:** "The Bitwise Shifter."

**The Plot:**

1. Initialize `res = 0`.
2. Iterate 32 times:
   - `res = (res << 1) | (n & 1)`: Shift result left to make room, add LSB of `n`.
   - `n >>= 1`: Process next bit of `n`.
3. Return `res`.

**The Twist (Failure):** **Logical Shift.** Ensure `n` is treated as unsigned so `>>` is logical (fills with 0) not arithmetic (fills with sign bit).

**Interview Signal:** Basic **Bit Manipulation**.

## 🚀 Approach & Intuition
Build result bit by bit.

### C++ Pseudo-Code
```cpp
uint32_t reverseBits(uint32_t n) {
    uint32_t res = 0;
    for (int i = 0; i < 32; i++) {
        res = (res << 1) | (n & 1);
        n >>= 1;
    }
    return res;
}
```

### Key Observations:

- Bitwise operations (AND, OR, XOR, NOT) allow for $O(1)$ constant time operations on binary data.
- XOR is particularly useful for finding single elements or toggling states, as $x \oplus x = 0$.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(1)$ (32 iterations)
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

- [Missing Number](../missing_number/PROBLEM.md) — Next in category
- [Counting Bits](../counting_bits/PROBLEM.md) — Previous in category
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
