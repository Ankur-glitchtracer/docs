#  🧩 DP: Regular Expression Matching

## 📝 Description
[LeetCode 10](https://leetcode.com/problems/regular-expression-matching/)
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:

- `.` Matches any single character.
- `*` Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Star (*)." It can match zero or more of the preceding element. This creates a branching decision tree. `a*` could match "", "a", "aa", "aaa"...

**The Hero:** "The Look-Back Logic."

**The Plot:**

1. Initialize `dp[s_len+1][p_len+1]`.
2. Base case: `dp[0][0] = true`. Handle patterns like `a*b*` matching empty string.
3. Nested loops for `i` (string) and `j` (pattern).
4. Apply transition logic.

**The Twist (Failure):** **Index Confusion.** `*` applies to `p[j-1]`. When `p[j] == '*'`, you care about `p[j-1]`.

**Interview Signal:** **Complex DP State Transitions**.

## 🚀 Approach & Intuition
Handle `*` by looking back 2 steps or consuming input.

### C++ Pseudo-Code
```cpp
bool isMatch(string s, string p) {
    int m = s.length(), n = p.length();
    vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
    dp[0][0] = true;
    
    // Handle patterns like a*, a*b*, etc. for empty string
    for (int j = 1; j <= n; j++) {
        if (p[j-1] == '*') dp[0][j] = dp[0][j-2];
    }
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (p[j-1] == '.' || p[j-1] == s[i-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else if (p[j-1] == '*') {
                dp[i][j] = dp[i][j-2]; // Zero count
                if (p[j-2] == '.' || p[j-2] == s[i-1]) {
                    dp[i][j] = dp[i][j] || dp[i-1][j]; // One+ count
                }
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

- [Burst Balloons](../burst_balloons/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
