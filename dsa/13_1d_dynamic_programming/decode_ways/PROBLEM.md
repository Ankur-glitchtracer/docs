#  🔐 DP: Decode Ways

## 📝 Description
[LeetCode 91](https://leetcode.com/problems/decode-ways/)
A message containing letters from A-Z can be encoded into numbers using the following mapping: 'A' -> "1", 'B' -> "2", ... 'Z' -> "26". Given a string `s` containing only digits, return the number of ways to decode it.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Leading Zero." '06' cannot be mapped to 'F'. Also, '10' is 'J', but '0' alone is invalid. The parsing logic is brittle.

**The Hero:** "The Fibonacci Decoder."

**The Plot:**

1. `dp[0] = 1` (Empty string has 1 way).
2. Iterate `i` from 1 to `n`.
3. If `s[i] != '0'`: `dp[i] += dp[i-1]`.
4. If `s[i-1]s[i]` is valid (10-26): `dp[i] += dp[i-2]`.

**The Twist (Failure):** **00.** A string like "100" or "05" has 0 ways. Handled correctly by checking `s[i] != '0'` and the validity of the pair.

**Interview Signal:** Handling **Edge Cases in DP**.

## 🚀 Approach & Intuition
Check single digit and two-digit validity.

### C++ Pseudo-Code
```cpp
int numDecodings(string s) {
    if (s[0] == '0') return 0;
    int n = s.length();
    int dp1 = 1; // dp[i-1]
    int dp2 = 1; // dp[i-2] (conceptually dp[-1])
    
    for (int i = 1; i < n; i++) {
        int current = 0;
        if (s[i] != '0') current += dp1;
        
        int twoDigit = stoi(s.substr(i-1, 2));
        if (twoDigit >= 10 && twoDigit <= 26) current += dp2;
        
        dp2 = dp1;
        dp1 = current;
    }
    return dp1;
}
```

### Key Observations:

- Break down the problem into smaller sub-problems and store their results to avoid redundant calculations.
- Determine the base cases and the recurrence relation; bottom-up (tabulation) is often more space-efficient.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (Optimized) or $O(N)$ (Array)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you optimize the space complexity from $O(N^2)$ to $O(N)$? Can you solve it using a top-down vs bottom-up approach?
- **Scale Question:** If the DP table is too large for memory, can you use 'Check-pointing' or a sliding window of rows to save space?
- **Edge Case Probe:** What are the base cases for empty or single-element inputs? How do you handle negative values if they aren't expected?

## 🔗 Related Problems

- [Coin Change](../coin_change/PROBLEM.md) — Next in category
- [Palindromic Substrings](../palindromic_substrings/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
