#  ⚡ Bit Manipulation: Single Number

## 📝 Description
[LeetCode 136](https://leetcode.com/problems/single-number/)
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

## 🛠️ Requirements/Constraints

- Inputs are typically 32-bit or 64-bit integers.
- The number of operations is $O(1)$ relative to word size.

## 🧠 The Engineering Story

**The Villain:** "The Memory Thief." Finding the unique number in a sea of duplicates. Using a Hash Set costs $O(N)$ space. On a memory-constrained chip, you only have $O(1)$.

**The Hero:** "The XOR Eraser." Using the bitwise XOR property: $A \oplus A = 0$ and $A \oplus 0 = A$.

**The Plot:**

1. Initialize `result = 0`.
2. Iterate through all numbers.
3. `result ^= num`.
4. All pairs will cancel each other out to
0. The unique number will remain.

**The Twist (Failure):** **The Triple Threat.** This ONLY works if numbers appear exactly twice. If some appear 3 times, you need to count set bits at each position modulo 3.

**Interview Signal:** Mastery of **Bitwise Logic** and $O(1)$ space optimization.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- Bitwise operations (AND, OR, XOR, NOT) allow for $O(1)$ constant time operations on binary data.
- XOR is particularly useful for finding single elements or toggling states, as $x \oplus x = 0$.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
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

- [Number of 1 Bits](../number_of_1_bits/PROBLEM.md) — Next in category
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
