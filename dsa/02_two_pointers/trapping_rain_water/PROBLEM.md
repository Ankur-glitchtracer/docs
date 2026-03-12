#  🌧️ Arrays: Trapping Rain Water

## 📝 Description
[LeetCode 42](https://leetcode.com/problems/trapping-rain-water/)
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## 🛠️ Requirements/Constraints

- $n == height.length$
- $1 \le n \le 2 \cdot 10^4$
- $0 \le height[i] \le 10^5$

## 🧠 The Engineering Story

**The Villain:** "The Scan-Heavy $O(N^2)$." For every single bar, scanning the entire left and right side to find the tallest boundaries.

**The Hero:** "The Two-Pointer Squeeze." Use two pointers at the ends and move the one with the shorter boundary inward, knowing that the shorter boundary is the limiting factor for water.

**The Plot:**

1. `left = 0`, `right = n-1`.
2. `left_max = 0`, `right_max = 0`.
3. If `height[left] < height[right]`:
   - If `height[left] >= left_max`, update `left_max`.
   - Else, add `left_max - height[left]` to total.
   - Move `left++`.
4. Else, do the same for the right side.

**The Twist (Failure):** **The Negative Water.** Forgetting that if the current bar is higher than the boundary, it traps zero water (not negative).

**Interview Signal:** Mastery of **Complex Two-Pointer Logic** and identifying limiting constraints.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- The amount of water at any point is determined by the minimum of the maximum heights to its left and right.
- The two-pointer approach can solve this in $O(N)$ time and $O(1)$ space by keeping track of `leftMax` and `rightMax`.

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

- **Harder Variant:** How would you solve this in 3D (Trapping Rain Water II) where you have a grid of heights?
- **Scale Question:** If the terrain is thousands of miles long, how would you use a MapReduce-like approach to calculate total water trapped?
- **Edge Case Probe:** How does the solution handle a 'V' shaped valley vs an 'A' shaped mountain?

## 🔗 Related Problems

- [Container With Most Water](../container_with_most_water/PROBLEM.md) — Previous in category
- [Best Time to Buy/Sell Stock](../../03_sliding_window/best_time_to_buy_sell_stock/PROBLEM.md) — Prerequisite for Sliding Window
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
- [Reverse Linked List](../../06_linked_list/reverse_list/PROBLEM.md) — Prerequisite for Linked List
