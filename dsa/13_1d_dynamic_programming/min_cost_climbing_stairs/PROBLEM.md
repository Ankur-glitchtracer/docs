#  🪜 DP: Min Cost Climbing Stairs

## 📝 Description
[LeetCode 746](https://leetcode.com/problems/min-cost-climbing-stairs/)
You are given an integer array `cost` where `cost[i]` is the cost of `i`th step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index `0`, or the step with index `1`. Return the minimum cost to reach the top of the floor.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Greedy Misstep." Picking the smaller cost at the current step might lead to a huge cost later. You can't just look one step ahead.

**The Hero:** "The Cumulative Cost Tracker." Calculate the minimum cost to *reach* step `i`, which relies on the costs of reaching `i-1` and `i-2`.

**The Plot:**

1. Let `dp[i]` be the min cost to reach step `i`.
2. Transition: `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`.
3. Base cases: `dp[0] = cost[0]`, `dp[1] = cost[1]`.
4. The result is `min(dp[n-1], dp[n-2])` because we can stop at either of the last two steps.

**The Twist (Failure):** **The Starting Step.** You can start at index 0 or 1. The recurrence naturally handles this if you consider the cost to *leave* step `i`.

**Interview Signal:** Basic **1D DP** optimization.

## 🚀 Approach & Intuition
Track min cost to reach current step.

### C++ Pseudo-Code
```cpp
int minCostClimbingStairs(vector<int>& cost) {
    int n = cost.size();
    int prev2 = cost[0];
    int prev1 = cost[1];
    
    for (int i = 2; i < n; i++) {
        int curr = cost[i] + min(prev1, prev2);
        prev2 = prev1;
        prev1 = curr;
    }
    return min(prev1, prev2);
}
```

### Key Observations:

- Break down the problem into smaller sub-problems and store their results to avoid redundant calculations.
- Determine the base cases and the recurrence relation; bottom-up (tabulation) is often more space-efficient.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (using two variables)

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

- [House Robber](../house_robber/PROBLEM.md) — Next in category
- [Climbing Stairs](../climbing_stairs/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
