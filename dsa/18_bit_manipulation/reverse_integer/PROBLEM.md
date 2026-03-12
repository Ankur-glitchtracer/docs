#  🔄 Bit Manipulation: Reverse Integer

## 📝 Description
[LeetCode 7](https://leetcode.com/problems/reverse-integer/)
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `(To be detailed...)`, then return `0`. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## 🛠️ Requirements/Constraints

- Inputs are typically 32-bit or 64-bit integers.
- The number of operations is $O(1)$ relative to word size.

## 🧠 The Engineering Story

**The Villain:** "The Overflow Trap." Reversing `1534236469` results in `9646324351`, which overflows a 32-bit signed integer.

**The Hero:** "The Pre-Check." Check for potential overflow *before* multiplying by 10.

**The Plot:**

1. Initialize `res = 0`.
2. While `x != 0`:
   - `pop = x % 10`, `x /= 10`.
   - **Check Positive Overflow:** If `res > INT_MAX/10` or `(res == INT_MAX/10 && pop > 7)`, return 0.
   - **Check Negative Overflow:** If `res < INT_MIN/10` or `(res == INT_MIN/10 && pop < -8)`, return 0.
   - `res = res * 10 + pop`.

**The Twist (Failure):** **Python/Java vs C++.** Python integers handle overflow automatically. C++ requires explicit checks.

**Interview Signal:** Handling **Integer Limits**.

## 🚀 Approach & Intuition
Modulo 10 to pop, Multiply 10 to push.

### C++ Pseudo-Code
```cpp
int reverse(int x) {
    int res = 0;
    while (x != 0) {
        int pop = x % 10;
        x /= 10;
        if (res > INT_MAX/10 || (res == INT_MAX/10 && pop > 7)) return 0;
        if (res < INT_MIN/10 || (res == INT_MIN/10 && pop < -8)) return 0;
        res = res * 10 + pop;
    }
    return res;
}
```

### Key Observations:

- Bitwise operations (AND, OR, XOR, NOT) allow for $O(1)$ constant time operations on binary data.
- XOR is particularly useful for finding single elements or toggling states, as $x \oplus x = 0$.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log x)$ (Digits)
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

- [Sum of Two Integers](../sum_of_two_integers/PROBLEM.md) — Previous in category
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
