#  ✖️ Math: Multiply Strings

## 📝 Description
[LeetCode 43](https://leetcode.com/problems/multiply-strings/)
Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string. Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

## 🛠️ Requirements/Constraints

- Numerical values fit within standard data types (int, long).
- Coordinate ranges are typically within $10^4$.

## 🧠 The Engineering Story

**The Villain:** "The Big Integer." Standard integer types (64-bit) can't hold the product of two 200-digit numbers.

**The Hero:** "The Grade-School Algorithm." Simulate manual multiplication using an array.

**The Plot:**

1. `num1` length `m`, `num2` length `n`. Result max length is `m+n`.
2. Create `res` array of size `m+n`.
3. Iterate `i` from `m-1` to 0, `j` from `n-1` to 0.
   - `mul = (num1[i] - '0') * (num2[j] - '0')`.
   - `p1 = i + j`, `p2 = i + j + 1`.
   - `sum = mul + res[p2]`.
   - `res[p2] = sum % 10`.
   - `res[p1] += sum / 10`.
4. Convert array to string, skipping leading zeros.

**The Twist (Failure):** **Zero.** If input is "0", output should be "0", not "".

**Interview Signal:** **Simulation** of arithmetic operations.

## 🚀 Approach & Intuition
Accumulate products at correct indices.

### C++ Pseudo-Code
```cpp
string multiply(string num1, string num2) {
    if (num1 == "0" || num2 == "0") return "0";
    int m = num1.size(), n = num2.size();
    vector<int> res(m + n, 0);
    
    for (int i = m - 1; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            int mul = (num1[i] - '0') * (num2[j] - '0');
            int p1 = i + j, p2 = i + j + 1;
            int sum = mul + res[p2];
            
            res[p2] = sum % 10;
            res[p1] += sum / 10;
        }
    }
    
    string s = "";
    for (int p : res) {
        if (!(s.empty() && p == 0)) s += to_string(p);
    }
    return s;
}
```

### Key Observations:

- Use modular arithmetic to prevent integer overflow and the Euclidean algorithm for GCD/LCM problems.
- In geometry, use cross products to determine orientation and the distance formula for proximity checks.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
    - **Space Complexity:** $O(M + N)$

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

- [Detect Squares](../detect_squares/PROBLEM.md) — Next in category
- [Pow(x, n)](../pow_x_n/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite: Bit Manipulation
