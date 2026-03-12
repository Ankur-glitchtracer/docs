#  🏠 DP: House Robber

## 📝 Description
[LeetCode 198](https://leetcode.com/problems/house-robber/)
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Alarm Trigger." Robbing adjacent houses triggers the alarm. You can't just rob the richest houses.

**The Hero:** "The Skip-or-Take Decider." At every house, you have two choices:

**The Plot:**

1. `rob[i] = max(nums[i] + rob[i-2], rob[i-1])`.
2. Optimize space: We only need `rob1` (i-2) and `rob2` (i-1).
3. Loop through houses updating `rob1` and `rob2`.

**The Twist (Failure):** **The Sequence.** `[2, 1, 1, 2]`. Greedy might pick `2, 2` (4). But `2, 1` (3)? No. The pattern isn't always "every other house". It's strictly about maximizing the sum.

**Interview Signal:** The quintessential **DP decision** problem.

## 🚀 Approach & Intuition
Maintain two variables for previous maximums.

### C++ Pseudo-Code
```cpp
int rob(vector<int>& nums) {
    int rob1 = 0, rob2 = 0;
    for (int n : nums) {
        int temp = max(n + rob1, rob2);
        rob1 = rob2;
        rob2 = temp;
    }
    return rob2;
}
```

### Key Observations:

- Break down the problem into smaller sub-problems and store their results to avoid redundant calculations.
- Determine the base cases and the recurrence relation; bottom-up (tabulation) is often more space-efficient.

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

- **Harder Variant:** Can you optimize the space complexity from $O(N^2)$ to $O(N)$? Can you solve it using a top-down vs bottom-up approach?
- **Scale Question:** If the DP table is too large for memory, can you use 'Check-pointing' or a sliding window of rows to save space?
- **Edge Case Probe:** What are the base cases for empty or single-element inputs? How do you handle negative values if they aren't expected?

## 🔗 Related Problems

- [House Robber II](../house_robber_ii/PROBLEM.md) — Next in category
- [Min Cost Climbing Stairs](../min_cost_climbing_stairs/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
