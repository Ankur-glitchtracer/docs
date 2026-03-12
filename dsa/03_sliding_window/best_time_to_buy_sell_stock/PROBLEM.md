#  📈 Arrays: Best Time to Buy and Sell Stock

## 📝 Description
[LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day. Find the maximum profit you can achieve.

## 🛠️ Requirements/Constraints

- $1 \le prices.length \le 10^5$
- $0 \le prices[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The $O(N^2)$ Pair Search." Checking every possible buy day and every possible sell day after it. For a decade of stock prices, this is 10M+ comparisons.

**The Hero:** "The One-Pass Min-Tracker." Keep track of the lowest price seen so far and calculate the potential profit at every step.

**The Plot:**

1. Maintain `min_price` (initialized to infinity) and `max_profit` (0).
2. For each price:
   - Update `min_price` if current price is lower.
   - Calculate `profit = current_price - min_price`.
   - Update `max_profit` if current profit is higher.

**The Twist (Failure):** **The Future Leak.** Trying to sell before you buy (checking `price[i] - price[i+1]`).

**Interview Signal:** Mastery of **Greedy One-Pass** algorithms.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- We only need to track the minimum price seen so far and the maximum profit possible if we sell today.
- This is a classic 'one-pass' problem that can be viewed as a variation of Kadane's algorithm.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the input is sorted or has a limited range? Can you optimize space from $O(N)$ to $O(1)$?
- **Scale Question:** If the dataset is too large to fit in RAM, how would you use external sorting or a distributed hash table?
- **Edge Case Probe:** How does your solution handle duplicates, empty inputs, or extremely large integers?

## 🔗 Related Problems

- [Longest Substring No Repeat](../longest_substring_without_repeating_characters/PROBLEM.md) — Next in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
