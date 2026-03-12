#  🎈 DP: Burst Balloons

## 📝 Description
[LeetCode 312](https://leetcode.com/problems/burst-balloons/)
You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons. If you burst the `i`th balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it. Return the maximum coins you can collect by bursting the balloons wisely.

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Dependency Hell." When you burst a balloon `i`, neighbors `i-1` and `i+1` become adjacent. This changes their potential values dynamically. Order matters immensely.

**The Hero:** "The Reverse Thinking." Instead of "Which balloon do I burst first?", ask "Which balloon do I burst **last**?".

**The Plot:**

1. If `k` is the last balloon to burst in range `(i, j)`, then `i` to `k-1` and `k+1` to `j` are independent subproblems!
2. `dp[i][j]` = Max coins from range `i` to `j`.
3. Iterate `length` from 1 to N.
4. Iterate `i` (start), `j` (end).
5. Iterate `k` (split) from `i` to `j`.
   - `coins = nums[i-1] * nums[k] * nums[j+1]` (Boundary values remain because `k` is last).
   - `dp[i][j] = max(dp[i][j], dp[i][k-1] + coins + dp[k+1][j])`.

**The Twist (Failure):** **Boundaries.** Add `1` to the start and end of the array to handle boundaries cleanly.

**Interview Signal:** **Interval DP** (Matrix Chain Multiplication variant).

## 🚀 Approach & Intuition
Determine the LAST balloon to burst in a range.

### C++ Pseudo-Code
```cpp
int maxCoins(vector<int>& nums) {
    int n = nums.size();
    vector<int> arr = {1};
    arr.insert(arr.end(), nums.begin(), nums.end());
    arr.push_back(1);
    
    vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
    
    for (int len = 1; len <= n; len++) {
        for (int i = 1; i <= n - len + 1; i++) {
            int j = i + len - 1;
            for (int k = i; k <= j; k++) {
                int coins = arr[i-1] * arr[k] * arr[j+1];
                coins += dp[i][k-1] + dp[k+1][j];
                dp[i][j] = max(dp[i][j], coins);
            }
        }
    }
    return dp[1][n];
}
```

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^3)$
    - **Space Complexity:** $O(N^2)$

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

- [Regular Expression Matching](../regular_expression_matching/PROBLEM.md) — Next in category
- [Edit Distance](../edit_distance/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
