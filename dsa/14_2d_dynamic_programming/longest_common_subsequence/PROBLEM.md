#  🧶 DP: Longest Common Subsequence

## 📝 Description
[LeetCode 1143](https://leetcode.com/problems/longest-common-subsequence/)
Given two strings `text1` and `text2`, return the length of their longest common subsequence.

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The String Matcher's Paradox." Comparing every subsequence of String A ($2^N$) with every subsequence of String B ($2^M$). The sun would burn out before you finished.

**The Hero:** "The 2D Grid Architect." Using a matrix to store the LCS length for all prefixes of both strings.

**The Plot:**

1. Create a matrix `dp[len1+1][len2+1]`.
2. For each char `i` in S1 and `j` in S2:
   - If `S1[i] == S2[j]`: They match! `dp[i][j] = 1 + dp[i-1][j-1]` (extend the previous match).
   - Else: Take the best of `dp[i-1][j]` or `dp[i][j-1]` (skip one char from either string).

**The Twist (Failure):** **The Off-by-One Matrix.** Forgetting the extra row/column for the empty string base case, leading to index errors.

**Interview Signal:** Mastery of **Multi-Dimensional DP** and string alignment logic.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
    - **Space Complexity:** $O(M 	imes N)$

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

- [Stock with Cooldown](../best_time_to_buy_and_sell_stock_with_cooldown/PROBLEM.md) — Next in category
- [Unique Paths](../unique_paths/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
