#  🚀 Math: Pow(x, n)

## 📝 Description
[LeetCode 50](https://leetcode.com/problems/powx-n/)
Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., $x^n$).

## 🛠️ Requirements/Constraints

- Numerical values fit within standard data types (int, long).
- Coordinate ranges are typically within $10^4$.

## 🧠 The Engineering Story

**The Villain:** "The Naive Multiplication." Multiplying $x$ by itself $n$ times takes $O(n)$. If $n = 2^{31}$, this times out.

**The Hero:** "Exponentiation by Squaring." $x^{10} = (x^5)^2$. $x^5 = x \cdot (x^2)^2$. We can halve $n$ at every step.

**The Plot:**

1. Handle negative $n$: $x = 1/x, n = -n$.
2. Base case: $n == 0$, return 1.
3. If $n$ is even: `half = myPow(x, n/2)`, return `half * half`.
4. If $n$ is odd: return `x * myPow(x, n-1)`.

**The Twist (Failure):** **Integer Overflow.** $n = -2^{31}$ (INT_MIN). If you do $n = -n$, it overflows positive INT_MAX. Use `long long` for $n$.

**Interview Signal:** **Divide and Conquer** / Logarithmic Math.

## 🚀 Approach & Intuition
Square the base, halve the exponent.

### C++ Pseudo-Code
```cpp
double myPow(double x, int n) {
    long long N = n;
    if (N < 0) {
        x = 1 / x;
        N = -N;
    }
    
    double res = 1;
    double current_product = x;
    
    while (N > 0) {
        if (N % 2 == 1) res *= current_product;
        current_product *= current_product;
        N /= 2;
    }
    return res;
}
```

### Key Observations:

- Use modular arithmetic to prevent integer overflow and the Euclidean algorithm for GCD/LCM problems.
- In geometry, use cross products to determine orientation and the distance formula for proximity checks.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log N)$
    - **Space Complexity:** $O(\log N)$ (Recursion stack)

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

- [Multiply Strings](../multiply_strings/PROBLEM.md) — Next in category
- [Plus One](../plus_one/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite: Bit Manipulation
