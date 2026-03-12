#  💧 Two Pointers: Container With Most Water

## 📝 Description
[LeetCode 11](https://leetcode.com/problems/container-with-most-water/)
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`. Find two lines that together with the x-axis form a container, such that the container contains the most water.

## 🛠️ Requirements/Constraints

- $n == height.length$
- $2 \le n \le 10^5$
- $0 \le height[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The All-Pairs Check." Trying every pair of lines ($O(N^2)$).

**The Hero:** "The Greedy Width Shrinker." We start with the maximum width. To find a potentially larger area, we must sacrifice width for greater height.

**The Plot:**

1. Initialize `left` and `right` at the ends.
2. Calculate `area = (right - left) * min(height[left], height[right])`.
3. Update `max_area`.
4. Move the pointer pointing to the *shorter* line inward. (Why? Because moving the taller line can only decrease width without increasing the limiting height).

**The Twist (Failure):** **The Equal Height.** If heights are equal, you can move either (or both).

**Interview Signal:** Understanding **Greedy Decisions** in optimization problems.

## 🚀 Approach & Intuition
Start wide and shrink, discarding the limiting line.

### C++ Pseudo-Code
```cpp
int maxArea(vector<int>& height) {
    int l = 0, r = height.size() - 1;
    int res = 0;
    while (l < r) {
        int area = (r - l) * min(height[l], height[r]);
        res = max(res, area);
        if (height[l] < height[r]) l++;
        else r--;
    }
    return res;
}
```

### Key Observations:

- The two-pointer approach starting from both ends is optimal because the width is maximized at the start.
- Always move the pointer pointing to the shorter line to potentially find a taller line that compensates for the decreasing width.

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

- **Harder Variant:** What if you need to find the container that can trap the most water (Trapping Rain Water)?
- **Scale Question:** How would you solve this if the 'heights' are a stream of data and you need to find the max container seen so far?
- **Edge Case Probe:** What if all heights are the same? What if the heights are strictly increasing or decreasing?

## 🔗 Related Problems

- [Trapping Rain Water](../trapping_rain_water/PROBLEM.md) — Next in category
- [3Sum](../3sum/PROBLEM.md) — Previous in category
- [Best Time to Buy/Sell Stock](../../03_sliding_window/best_time_to_buy_sell_stock/PROBLEM.md) — Prerequisite for Sliding Window
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
