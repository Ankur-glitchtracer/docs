#  📈 DP: Longest Increasing Subsequence

## 📝 Description
[LeetCode 300](https://leetcode.com/problems/longest-increasing-subsequence/)
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Non-Contiguous Nightmare." Unlike substrings, subsequences can skip elements, making a simple window approach impossible.

**The Hero:** "The Look-Back Optimizer." For every element, looking back at all previous elements to see which one it can extend.

**The Plot:**

1. `dp[i]` represents the length of LIS ending at index `i`.
2. Initialize all `dp[i] = 1`.
3. For `i` from 1 to `n`:
   - For `j` from 0 to `i-1`:
     - If `nums[i] > nums[j]`, then `dp[i] = max(dp[i], 1 + dp[j])`.
4. Result is `max(dp)`.

**The Twist (Failure):** **The $O(N^2)$ Wall.** For $N > 10,000$, this approach is too slow. The "Ultimate Hero" uses Binary Search + Patience Sorting to solve it in $O(N \log N)$.

**Interview Signal:** Mastery of **1D DP** and identifying optimal sub-structure.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- Break down the problem into smaller sub-problems and store their results to avoid redundant calculations.
- Determine the base cases and the recurrence relation; bottom-up (tabulation) is often more space-efficient.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2)$ (Standard DP)
    - **Space Complexity:** $O(N)$

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

- [Partition Equal Subset Sum](../partition_equal_subset_sum/PROBLEM.md) — Next in category
- [Word Break](../word_break/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
