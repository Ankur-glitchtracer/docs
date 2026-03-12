#  📉 DP: Best Time to Buy and Sell Stock with Cooldown

## 📝 Description
[LeetCode 309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
- Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## 🛠️ Requirements/Constraints

- $M, N \le 1000$
- Time complexity is typically $O(M \cdot N)$.

## 🧠 The Engineering Story

**The Villain:** "The State Complexity." You can't just buy/sell whenever. You have a "Cooldown" state. This creates dependencies between actions across 2 days.

**The Hero:** "The State Machine." Define 3 states:

**The Plot:**

1. `held[i] = max(held[i-1], reset[i-1] - price)`.
2. `sold[i] = held[i-1] + price`.
3. `reset[i] = max(reset[i-1], sold[i-1])`.
4. Initial: `held = -inf`, `sold = 0`, `reset = 0`.

**The Twist (Failure):** **The Initial State.** If you start with `held = 0`, it means you bought a stock for free. Wrong. It must be `-infinity` or `-prices[0]` if day 0 logic allows.

**Interview Signal:** Modeling **State Machines** with DP.

## 🚀 Approach & Intuition
Track states: Hold, Sold, Rest.

### C++ Pseudo-Code
```cpp
int maxProfit(vector<int>& prices) {
    int sold = 0;
    int hold = INT_MIN;
    int rest = 0;
    
    for (int p : prices) {
        int prevSold = sold;
        sold = hold + p;
        hold = max(hold, rest - p);
        rest = max(rest, prevSold);
    }
    return max(sold, rest);
}
```

### Key Observations:

- 2D DP is common for string comparison (LCS, Edit Distance) or matrix-based pathfinding.
- Space can often be optimized from $O(M \cdot N)$ to $O(N)$ by only keeping the previous row or column.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (3 variables)

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

- [Coin Change II](../coin_change_ii/PROBLEM.md) — Next in category
- [Longest Common Subsequence](../longest_common_subsequence/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite: 1-D Dynamic Programming
