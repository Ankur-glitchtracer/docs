#  🕵️ Bit Manipulation: Missing Number

## 📝 Description
[LeetCode 268](https://leetcode.com/problems/missing-number/)
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

## 🛠️ Requirements/Constraints

- Inputs are typically 32-bit or 64-bit integers.
- The number of operations is $O(1)$ relative to word size.

## 🧠 The Engineering Story

**The Villain:** "The Sum Overflow." Summing `0..n` using `n*(n+1)/2` might overflow if `n` is huge (though usually fine for `int`). Sorting is $O(N \log N)$. Hash Set is $O(N)$ space.

**The Hero:** "The XOR Cancellation."

**The Plot:**

1. XOR all numbers `0` to `n`.
2. XOR all numbers in `nums`.
3. `Result = (XOR of range) ^ (XOR of array)`.
4. Everything present cancels out. Only the missing number remains.

**The Twist (Failure):** **The Index Loop.** You can do it in one loop: `res ^= i ^ nums[i]`, but array is size `n` (missing one), range is size `n+1`. XOR `n` separately.

**Interview Signal:** **XOR Properties**.

## 🚀 Approach & Intuition
XOR indices and values.

### C++ Pseudo-Code
```cpp
int missingNumber(vector<int>& nums) {
    int res = nums.size();
    for (int i = 0; i < nums.size(); i++) {
        res ^= i ^ nums[i];
    }
    return res;
}
```

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

- [Sum of Two Integers](../sum_of_two_integers/PROBLEM.md) — Next in category
- [Reverse Bits](../reverse_bits/PROBLEM.md) — Previous in category
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
