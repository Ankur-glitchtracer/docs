#  💰 DP: Coin Change

## 📝 Description
[LeetCode 322](https://leetcode.com/problems/coin-change/)
You are given an integer array `coins` and an integer `amount`. Return the fewest number of coins that you need to make up that amount.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Greedy Failure." Thinking you can always pick the largest coin first (e.g., if coins are [1, 3, 4] and target is 6, Greedy picks 4+1+1=3 coins, but the Hero knows 3+3=2 coins is better).

**The Hero:** "The Min-Cost Tabulator." Building a table of the minimum coins needed for every amount from 0 to `amount`.

**The Plot:**

1. Initialize `dp` array of size `amount + 1` with `infinity`, and `dp[0] = 0`.
2. For every amount `i` from 1 to `amount`:
   - For every coin `c`:
     - If `i - c >= 0`, then `dp[i] = min(dp[i], 1 + dp[i-c])`.
3. If `dp[amount]` is still `infinity`, return -1.

**The Twist (Failure):** **The Default Value.** Using `0` as a default instead of `infinity` makes every `min()` call return 0, breaking the logic.

**Interview Signal:** Mastery of **Unbounded Knapsack** and identifying why Greedy fails.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- Break down the problem into smaller sub-problems and store their results to avoid redundant calculations.
- Determine the base cases and the recurrence relation; bottom-up (tabulation) is often more space-efficient.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N 	imes 	ext{amount})$
    - **Space Complexity:** $O(	ext{amount})$

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

- [Max Product Subarray](../maximum_product_subarray/PROBLEM.md) — Next in category
- [Decode Ways](../decode_ways/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
