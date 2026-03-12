#  1️⃣ Bit Manipulation: Number of 1 Bits

## 📝 Description
[LeetCode 191](https://leetcode.com/problems/number-of-1-bits/)
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

## 🛠️ Requirements/Constraints

- Inputs are typically 32-bit or 64-bit integers.
- The number of operations is $O(1)$ relative to word size.

## 🧠 The Engineering Story

**The Villain:** "The Loop 32." Iterating 32 times for every integer, checking `n & 1`.

**The Hero:** "The Brian Kernighan's Algorithm." Jumping directly to the set bits.

**The Plot:**

1. While `n != 0`:
   - `n = n & (n - 1)`.
   - This operation flips the *least significant set bit* to 0.
   - `count++`.
2. Return count.

**The Twist (Failure):** **Efficiency.** If a number has only 1 set bit (e.g., $2^{30}$), Kernighan's loop runs 1 time. The naive loop runs 32 times.

**Interview Signal:** Mastery of **Bitwise Tricks**.

## 🚀 Approach & Intuition
Clear least significant bit repeatedly.

### C++ Pseudo-Code
```cpp
int hammingWeight(uint32_t n) {
    int count = 0;
    while (n) {
        n = n & (n - 1);
        count++;
    }
    return count;
}
```

### Key Observations:

- Bitwise operations (AND, OR, XOR, NOT) allow for $O(1)$ constant time operations on binary data.
- XOR is particularly useful for finding single elements or toggling states, as $x \oplus x = 0$.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(1)$ (Technically $O(	ext{set bits})$).
    - **Space Complexity:** $O(1)$.

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

- [Counting Bits](../counting_bits/PROBLEM.md) — Next in category
- [Single Number](../single_number/PROBLEM.md) — Previous in category
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
