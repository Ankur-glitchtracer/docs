#  💰 DP: Coin Change II

## 📝 Description
[LeetCode 518](https://leetcode.com/problems/coin-change-2/)
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0. You may assume that you have an infinite number of each kind of coin.

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The Combination Count." Coin Change I asked for the *minimum* coins. Now we want the *number of ways*.

**The Hero:** "The Unbounded Knapsack Count."

**The Plot:**

1. `dp[i]` = Number of ways to make amount `i`.
2. `dp[0] = 1`.
3. **Outer Loop (Coins):** For each coin `c`.
4. **Inner Loop (Amounts):** For `i` from `c` to `amount`:
   - `dp[i] += dp[i - c]`.

**The Twist (Failure):** **Swapping Loops.** If you loop `Amount` then `Coins` (`for i in amount: for c in coins`), you calculate **Permutations** (e.g., `1+2` and `2+1` are counted distinct). The problem asks for **Combinations**. You must process one coin fully before moving to the next.

**Interview Signal:** Distinction between **Permutations and Combinations** in DP.

## 🚀 Approach & Intuition
Outer loop coins, inner loop amounts.

### C++ Pseudo-Code
```cpp
int change(int amount, vector<int>& coins) {
    vector<int> dp(amount + 1, 0);
    dp[0] = 1;
    for (int c : coins) {
        for (int i = c; i <= amount; i++) {
            dp[i] += dp[i - c];
        }
    }
    return dp[amount];
}
```

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot \text{Amount})$
    - **Space Complexity:** $O(\text{Amount})$

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

- [Target Sum](../target_sum/PROBLEM.md) — Next in category
- [Stock with Cooldown](../best_time_to_buy_and_sell_stock_with_cooldown/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
