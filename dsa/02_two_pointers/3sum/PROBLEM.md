#  3️⃣ Two Pointers: 3Sum

## 📝 Description
[LeetCode 15](https://leetcode.com/problems/3sum/)
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

## 🛠️ Requirements/Constraints

- $3 \le nums.length \le 3000$
- $-10^5 \le nums[i] \le 10^5$

## 🧠 The Engineering Story

**The Villain:** "The Cubic Nightmare." Three nested loops giving $O(N^3)$. With $N=3000$, this will time out.

**The Hero:** "The Sorted Fixer." Fix one number, then use Two Sum (Two Pointers) on the rest.

**The Plot:**

1. Sort the array ($O(N \log N)$).
2. Iterate `i` from 0 to `n-2`.
3. If `nums[i] > 0`, break (sum can't be 0).
4. If `i > 0` and `nums[i] == nums[i-1]`, skip to avoid duplicates.
5. Use Two Pointers (`l`, `r`) on the subarray `i+1` to `n-1` to find pairs summing to `-nums[i]`.

**The Twist (Failure):** **The Triplet Duplicates.** Finding `[-1, 0, 1]` multiple times. You must skip duplicate values for `l` and `r` after finding a valid triplet.

**Interview Signal:** Handling **Duplicate Reduction** in combinatorial problems.

## 🚀 Approach & Intuition
Fix one element and find the other two.

### C++ Pseudo-Code
```cpp
vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    for (int i = 0; i < nums.size(); i++) {
        if (i > 0 && nums[i] == nums[i-1]) continue;
        int l = i + 1, r = nums.size() - 1;
        while (l < r) {
            int sum = nums[i] + nums[l] + nums[r];
            if (sum > 0) r--;
            else if (sum < 0) l++;
            else {
                res.push_back({nums[i], nums[l], nums[r]});
                l++;
                while (l < r && nums[l] == nums[l-1]) l++;
            }
        }
    }
    return res;
}
```

### Key Observations:

- Sorting the array ($O(N \log N)$) is necessary to use the two-pointer technique effectively and handle duplicates.
- Fix one element and solve the Two Sum II problem for the remaining target, skipping duplicate elements to avoid redundant triplets.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2)$
    - **Space Complexity:** $O(1)$ (ignoring output)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you find four numbers that sum to a target (4Sum)? How about $K$ numbers (K-Sum)?
- **Scale Question:** If the input has 1 million numbers, how can you optimize the search to avoid the $O(N^2)$ bottleneck? (e.g., parallelizing the outer loop).
- **Edge Case Probe:** How do you efficiently skip duplicate triplets without using a hash set for the final results?

## 🔗 Related Problems

- [Container With Most Water](../container_with_most_water/PROBLEM.md) — Next in category
- [Two Sum II](../two_sum_ii/PROBLEM.md) — Previous in category
- [Best Time to Buy/Sell Stock](../../03_sliding_window/best_time_to_buy_sell_stock/PROBLEM.md) — Prerequisite for Sliding Window
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
