#  ⚖️ DP: Partition Equal Subset Sum

## 📝 Description
[LeetCode 416](https://leetcode.com/problems/partition-equal-subset-sum/)
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Half-Sum Search." We need to find a subset that sums to `Total / 2`.

**The Hero:** "The 0/1 Knapsack." This is exactly Knapsack where item weights = values, and capacity = `Total / 2`.

**The Plot:**

1. Calculate `total_sum`. If odd, return False.
2. `target = total_sum / 2`.
3. Use a Set (or boolean array) `dp` initialized with `{0}`.
4. For each number `n` in `nums`:
   - Create `new_dp`.
   - For each `t` in `dp`: add `t + n` to `new_dp`.
   - `dp = dp U new_dp`.
5. If `target` in `dp`, return True.

**The Twist (Failure):** **Iterating the Set.** Using a Set is often faster than a fixed array if the number of reachable sums is small. Array works best if sums are dense.

**Interview Signal:** Reduction to **Knapsack**.

## 🚀 Approach & Intuition
Track all reachable sums.

### C++ Pseudo-Code
```cpp
bool canPartition(vector<int>& nums) {
    int sum = accumulate(nums.begin(), nums.end(), 0);
    if (sum % 2 != 0) return false;
    int target = sum / 2;
    
    unordered_set<int> dp;
    dp.insert(0);
    
    for (int n : nums) {
        unordered_set<int> nextDP;
        for (int t : dp) {
            if (t + n == target) return true;
            nextDP.insert(t + n);
            nextDP.insert(t);
        }
        dp = nextDP;
    }
    return dp.count(target);
}
```

### Key Observations:

- Break down the problem into smaller sub-problems and store their results to avoid redundant calculations.
- Determine the base cases and the recurrence relation; bottom-up (tabulation) is often more space-efficient.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot \text{Sum})$.
    - **Space Complexity:** $O(\text{Sum})$.

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

- [Longest Increasing Subseq](../longest_increasing_subsequence/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
- [Subsets](../../10_backtracking/subsets/PROBLEM.md) — Prerequisite: Backtracking
