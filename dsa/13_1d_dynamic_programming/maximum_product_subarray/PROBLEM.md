#  ✖️ DP: Maximum Product Subarray

## 📝 Description
[LeetCode 152](https://leetcode.com/problems/maximum-product-subarray/)
Given an integer array `nums`, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Negative Flip." A negative number can turn a huge positive product into a huge negative one, OR a huge negative product into a massive positive one.

**The Hero:** "The Min-Max Tracker." We must track *both* the maximum and minimum product ending at the current position.

**The Plot:**

1. Initialize `res`, `curMax`, `curMin` to `nums[0]`.
2. Iterate `n` in `nums[1:]`:
   - If `n` is negative, swap `curMax` and `curMin`. (Because max * neg = min, min * neg = max).
   - `curMax = max(n, curMax * n)`.
   - `curMin = min(n, curMin * n)`.
   - `res = max(res, curMax)`.

**The Twist (Failure):** **Zero.** If `n` is 0, `curMax` and `curMin` reset to 0. The logic handles this (next iteration starts fresh from `n`), but be aware that 0 kills the streak.

**Interview Signal:** Managing **Dual States**.

## 🚀 Approach & Intuition
Maintain both extremes to handle negative multiplications.

### C++ Pseudo-Code
```cpp
int maxProduct(vector<int>& nums) {
    int res = *max_element(nums.begin(), nums.end());
    int curMin = 1, curMax = 1;
    
    for (int n : nums) {
        if (n == 0) {
            curMin = 1;
            curMax = 1;
            continue;
        }
        int tmp = curMax * n;
        curMax = max({n * curMax, n * curMin, n});
        curMin = min({tmp, n * curMin, n});
        res = max(res, curMax);
    }
    return res;
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

- [Word Break](../word_break/PROBLEM.md) — Next in category
- [Coin Change](../coin_change/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
