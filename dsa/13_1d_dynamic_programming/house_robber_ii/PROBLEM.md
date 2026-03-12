#  🏠 DP: House Robber II

## 📝 Description
[LeetCode 213](https://leetcode.com/problems/house-robber-ii/)
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Circular Neighborhood." The street is a circle. The first and last houses are neighbors. You can't rob both.

**The Hero:** "The Two-Pass Solver." Break the circle into two linear problems:

**The Plot:**

1. If `nums` has 1 element, return it.
2. Run standard House Robber on `nums[0...n-2]`.
3. Run standard House Robber on `nums[1...n-1]`.
4. Return `max(result1, result2)`.

**The Twist (Failure):** **The Single House.** If array has 1 element, slicing `0:-1` gives empty. Handle edge case.

**Interview Signal:** **Problem Reduction** (Circular to Linear).

## 🚀 Approach & Intuition
Run House Robber twice: once excluding first, once excluding last.

### C++ Pseudo-Code
```cpp
int rob(vector<int>& nums) {
    if (nums.empty()) return 0;
    if (nums.size() == 1) return nums[0];
    
    auto robLinear = [](vector<int>& arr, int start, int end) {
        int rob1 = 0, rob2 = 0;
        for (int i = start; i <= end; i++) {
            int temp = max(arr[i] + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        return rob2;
    };
    
    return max(robLinear(nums, 0, nums.size() - 2), 
               robLinear(nums, 1, nums.size() - 1));
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

- [Longest Palindromic Substring](../longest_palindromic_substring/PROBLEM.md) — Next in category
- [House Robber](../house_robber/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
