#  🎯 DP: Target Sum

## 📝 Description
[LeetCode 494](https://leetcode.com/problems/target-sum/)
You are given an integer array `nums` and an integer `target`. You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers. Return the number of different expressions that you can build, which evaluates to `target`.

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Sign Flipper." You have to assign `+` or `-` to every number. $2^N$ combinations.

**The Hero:** "The Subset Sum Transformation."

**The Plot:**

1. Check if `(Target + TotalSum)` is even and non-negative. If not, return 0.
2. Find the number of subsets that sum to `(Target + TotalSum) / 2`.
3. This is exactly **0/1 Knapsack (Count Ways)**.

**The Twist (Failure):** **The Zero.** If the array contains 0s, standard subset sum might undercount if not handled carefully (0 can be +0 or -0, effectively doubling ways for each zero). DP handles this naturally if iterated correctly.

**Interview Signal:** **Math Reduction** to simplify search space.

## 🚀 Approach & Intuition
Find subset with sum `(total + target) / 2`.

### C++ Pseudo-Code
```cpp
int findTargetSumWays(vector<int>& nums, int target) {
    long total = accumulate(nums.begin(), nums.end(), 0);
    if ((total + target) % 2 != 0 || abs(target) > total) return 0;
    
    int newTarget = (total + target) / 2;
    vector<int> dp(newTarget + 1, 0);
    dp[0] = 1;
    
    for (int n : nums) {
        for (int i = newTarget; i >= n; i--) {
            dp[i] += dp[i - n];
        }
    }
    return dp[newTarget];
}
```

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot \text{Sum})$
    - **Space Complexity:** $O(\text{Sum})$

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

- [Interleaving String](../interleaving_string/PROBLEM.md) — Next in category
- [Coin Change II](../coin_change_ii/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
