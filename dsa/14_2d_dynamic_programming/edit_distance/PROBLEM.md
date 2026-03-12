#  ✏️ DP: Edit Distance

## 📝 Description
[LeetCode 72](https://leetcode.com/problems/edit-distance/)
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Typo Fixer." Transforming "horse" to "ros". Insert? Delete? Replace? The search space of operations is huge.

**The Hero:** "The Levenshtein Distance." `dp[i][j]` = min ops to convert `word1[0...i]` to `word2[0...j]`.

**The Plot:**

1. Base Cases:
   - `dp[i][0] = i` (Delete all chars from word1).
   - `dp[0][j] = j` (Insert all chars to word1).
2. Transition:
   - If `word1[i] == word2[j]`: No op needed. `dp[i][j] = dp[i-1][j-1]`.
   - If mismatch, take `1 + min` of:
     - `dp[i-1][j]` (Delete)
     - `dp[i][j-1]` (Insert)
     - `dp[i-1][j-1]` (Replace)

**The Twist (Failure):** **Index Alignment.** `dp` table is usually size `(M+1)x(N+1)`. `word[i-1]` corresponds to `dp[i]`. Careful with off-by-one.

**Interview Signal:** The "Hello World" of **String DP**.

## 🚀 Approach & Intuition
Minimize cost of Insert, Delete, Replace.

### C++ Pseudo-Code
```cpp
int minDistance(string word1, string word2) {
    int m = word1.length(), n = word2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    
    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
            }
        }
    }
    return dp[m][n];
}
```

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
    - **Space Complexity:** $O(M 	imes N)$ (or $O(min(M, N))$ with 1D optimization)

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

- [Burst Balloons](../burst_balloons/PROBLEM.md) — Next in category
- [Distinct Subsequences](../distinct_subsequences/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
