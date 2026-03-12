#  🧶 DP: Distinct Subsequences

## 📝 Description
[LeetCode 115](https://leetcode.com/problems/distinct-subsequences/)
Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Many Matches." `s = "rabbbit"`, `t = "rabbit"`. The 'b's can be matched in multiple ways. Counting permutations is hard.

**The Hero:** "The 2D Counter." `dp[i][j]` = Number of ways to form `t[0...j]` from `s[0...i]`.

**The Plot:**

1. Base Case: `dp[i][0] = 1` (Empty `t` can be formed from any `s` by deleting everything).
2. Transition:
   - If `s[i-1] == t[j-1]`:
     - We can use this char: `dp[i-1][j-1]` ways.
     - OR we can skip this char: `dp[i-1][j]` ways.
     - Total: `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`.
   - If mismatch:
     - We MUST skip `s[i-1]`: `dp[i][j] = dp[i-1][j]`.

**The Twist (Failure):** **Overflow.** The number of ways can exceed 2^31. Use `unsigned long long` or `double` (if only count magnitude matters, though LeetCode guarantees it fits in `long long` usually, but some tests are huge).

**Interview Signal:** **Matching Logic** in DP.

## 🚀 Approach & Intuition
Match or skip characters.

### C++ Pseudo-Code
```cpp
int numDistinct(string s, string t) {
    int m = s.length(), n = t.length();
    vector<unsigned long long> dp(n + 1, 0);
    dp[0] = 1;
    
    for (int i = 1; i <= m; i++) {
        for (int j = n; j >= 1; j--) {
            if (s[i-1] == t[j-1]) {
                dp[j] = dp[j] + dp[j-1];
            }
        }
    }
    return dp[n];
}
```

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
    - **Space Complexity:** $O(N)$ (1D Optimization)

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

- [Edit Distance](../edit_distance/PROBLEM.md) — Next in category
- [Longest Increasing Path](../longest_increasing_path_in_matrix/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
