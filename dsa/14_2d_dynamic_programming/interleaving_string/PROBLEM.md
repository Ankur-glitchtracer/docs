#  🔀 DP: Interleaving String

## 📝 Description
[LeetCode 97](https://leetcode.com/problems/interleaving-string/)
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`. An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that `s3` is formed by concatenating these substrings in order while maintaining the relative order of characters from `s` and `t`.

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Ambiguous Path." `s1=aab`, `s2=aac`. `s3=aaabac`. The first `aa` in `s3` could come from `s1` OR `s2`. Greedy matching fails because making the "wrong" choice early blocks the solution later.

**The Hero:** "The 2D Path Validator." `dp[i][j]` = Can we form `s3[0...i+j]` using `s1[0...i]` and `s2[0...j]`?

**The Plot:**

1. Base Case: `dp[0][0] = true`.
2. Transition: `dp[i][j]` is true IF:
   - (`dp[i-1][j]` is true AND `s1[i-1] == s3[i+j-1]`)
   - OR
   - (`dp[i][j-1]` is true AND `s2[j-1] == s3[i+j-1]`)

**The Twist (Failure):** **Space Optimization.** You only need the previous row (or column). 1D DP array works fine.

**Interview Signal:** **String Merging** logic.

## 🚀 Approach & Intuition
Check reachable states (i, j).

### C++ Pseudo-Code
```cpp
bool isInterleave(string s1, string s2, string s3) {
    int m = s1.length(), n = s2.length();
    if (m + n != s3.length()) return false;
    
    vector<bool> dp(n + 1, false);
    
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 && j == 0) dp[j] = true;
            else {
                bool fromS1 = i > 0 && dp[j] && s1[i-1] == s3[i+j-1];
                bool fromS2 = j > 0 && dp[j-1] && s2[j-1] == s3[i+j-1];
                dp[j] = fromS1 || fromS2;
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
    - **Space Complexity:** $O(N)$ (1D optimization)

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

- [Longest Increasing Path](../longest_increasing_path_in_matrix/PROBLEM.md) — Next in category
- [Target Sum](../target_sum/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
