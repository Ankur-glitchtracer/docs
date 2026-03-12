#  ➕ Bit Manipulation: Sum of Two Integers

## 📝 Description
[LeetCode 371](https://leetcode.com/problems/sum-of-two-integers/)
Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.

## 🛠️ Requirements/Constraints

- Inputs are typically 32-bit or 64-bit integers.
- The number of operations is $O(1)$ relative to word size.

## 🧠 The Engineering Story

**The Villain:** "The Forbidden Plus." Add two numbers without `+` or `-`.

**The Hero:** "The Logic Gate Adder."

**The Plot:**

1. While `carry != 0`:
   - `sum = a ^ b`
   - `carry = (a & b) << 1`
   - `a = sum`, `b = carry`
2. Return `a`.

**The Twist (Failure):** **Negative Numbers.** In C++, left shifting a negative number is undefined behavior. Cast to `unsigned` before shifting. Python handles integers arbitrarily large, so mask with `0xFFFFFFFF`.

**Interview Signal:** **Circuit Logic** simulation.

## 🚀 Approach & Intuition
XOR for sum, AND for carry.

### C++ Pseudo-Code
```cpp
int getSum(int a, int b) {
    while (b != 0) {
        int carry = (unsigned int)(a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}
```

### Key Observations:

- Bitwise operations (AND, OR, XOR, NOT) allow for $O(1)$ constant time operations on binary data.
- XOR is particularly useful for finding single elements or toggling states, as $x \oplus x = 0$.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(1)$ (Max 32 bits)
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

- [Reverse Integer](../reverse_integer/PROBLEM.md) — Next in category
- [Missing Number](../missing_number/PROBLEM.md) — Previous in category
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
