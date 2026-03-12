#  ➕ Math: Plus One

## 📝 Description
[LeetCode 66](https://leetcode.com/problems/plus-one/)
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

## 🛠️ Requirements/Constraints

- Numerical values fit within standard data types (int, long).
- Coordinate ranges are typically within $10^4$.

## 🧠 The Engineering Story

**The Villain:** "The Domino Effect." Adding 1 to 999 requires carrying over 1 three times to get 1000.

**The Hero:** "The Carry Propagator."

**The Plot:**

1. Iterate backwards from the last digit.
2. If digit < 9: Increment and return. We are done (no more carry).
3. If digit == 9: Set to
0. Continue loop (carry propagates).
4. **The Twist:** If loop finishes (e.g., 99 -> 00), we need a new leading 1.
   - Resize array or insert 1 at beginning.
   - Or create new array of size $N+1$ with `1` followed by zeros.

**The Twist (Failure):** (To be detailed...)

**Interview Signal:** Basic **Array Manipulation** and edge cases.

## 🚀 Approach & Intuition
Propagate carry.

### C++ Pseudo-Code
```cpp
vector<int> plusOne(vector<int>& digits) {
    int n = digits.size();
    for (int i = n - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            return digits;
        }
        digits[i] = 0;
    }
    
    digits.insert(digits.begin(), 1);
    return digits;
}
```

### Key Observations:

- Use modular arithmetic to prevent integer overflow and the Euclidean algorithm for GCD/LCM problems.
- In geometry, use cross products to determine orientation and the distance formula for proximity checks.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (if resizing in place)

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

- [Pow(x, n)](../pow_x_n/PROBLEM.md) — Next in category
- [Happy Number](../happy_number/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite: Bit Manipulation
