#  😄 Math: Happy Number

## 📝 Description
[LeetCode 202](https://leetcode.com/problems/happy-number/)
Write an algorithm to determine if a number `n` is happy. A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

## 🛠️ Requirements/Constraints

- Numerical values fit within standard data types (int, long).
- Coordinate ranges are typically within $10^4$.

## 🧠 The Engineering Story

**The Villain:** "The Infinite Loop." Summing squares of digits can cycle forever (e.g., 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4...).

**The Hero:** "The Cycle Detective." This is exactly like Linked List Cycle! The sequence of numbers forms a linked list.

**The Plot:**

1. Use **Floyd's Cycle-Finding Algorithm** (Tortoise and Hare) OR a Hash Set.
2. **Tortoise:** Calculate next sum once.
3. **Hare:** Calculate next sum twice.
4. If they meet at 1: Happy!
5. If they meet at not 1: Cycle detected (Unhappy).

**The Twist (Failure):** **Number Growth.** Does the sum grow to infinity? No. For 999, sum is $81*3 = 243$. Any number $>= 1000$ reduces to $< 1000$. So it must eventually cycle or hit 1.

**Interview Signal:** Identifying **Cycles** in state transitions.

## 🚀 Approach & Intuition
Detect loop in sum sequence.

### C++ Pseudo-Code
```cpp
int sumSquares(int n) {
    int sum = 0;
    while (n) {
        int d = n % 10;
        sum += d * d;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow = n, fast = sumSquares(n);
    while (fast != 1 && slow != fast) {
        slow = sumSquares(slow);
        fast = sumSquares(sumSquares(fast));
    }
    return fast == 1;
}
```

### Key Observations:

- Use modular arithmetic to prevent integer overflow and the Euclidean algorithm for GCD/LCM problems.
- In geometry, use cross products to determine orientation and the distance formula for proximity checks.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log N)$ (Number of digits is log N)
    - **Space Complexity:** $O(1)$ (Floyd's) or $O(\log N)$ (Set)

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

- [Plus One](../plus_one/PROBLEM.md) — Next in category
- [Set Matrix Zeroes](../set_matrix_zeroes/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite: Bit Manipulation
