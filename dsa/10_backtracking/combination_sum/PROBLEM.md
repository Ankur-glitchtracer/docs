#  🎯 Backtracking: Combination Sum

## 📝 Description
[LeetCode 39](https://leetcode.com/problems/combination-sum/)
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order. The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Infinite Re-use." Unlike Subsets, you can reuse the same number infinitely. A simple loop causes infinite recursion (e.g., `2, 2, 2...` trying to reach 7).

**The Hero:** "The Controlled Repetition." We still have a choice: Pick `nums[i]` again, or move to `nums[i+1]`.

**The Plot:**

1. Base Case 1: `target == 0` -> Valid combination found. Add to results.
2. Base Case 2: `target < 0` or `index >= nums.length` -> Invalid path. Return.
3. **Branch 1 (Reuse):** Add `nums[i]`, recurse with `target - nums[i]` and SAME `index`.
4. **Branch 2 (Skip):** Backtrack (remove `nums[i]`), recurse with ORIGINAL `target` and `index + 1`.

**The Twist (Failure):** **The Duplicate Sets.** Why `index` instead of `0` in the loop? If we restarted from 0, we'd get `[2,3]` and `[3,2]`. Keeping `i` ensures we only move forward, preventing duplicate combinations.

**Interview Signal:** Handling **Unbounded Knapsack** variants via recursion.

## 🚀 Approach & Intuition
Reuse current index for inclusion, move index for exclusion.

### C++ Pseudo-Code
```cpp
vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    vector<vector<int>> res;
    vector<int> curr;
    
    function<void(int, int)> backtrack = [&](int i, int total) {
        if (total == target) {
            res.push_back(curr);
            return;
        }
        if (i >= candidates.size() || total > target) return;
        
        // Include candidates[i]
        curr.push_back(candidates[i]);
        backtrack(i, total + candidates[i]);
        curr.pop_back();
        
        // Skip candidates[i]
        backtrack(i + 1, total);
    };
    
    backtrack(0, 0);
    return res;
}
```

### Key Observations:

- Backtracking is essentially a DFS on a state-space tree where we 'undo' the last move to explore other branches.
- Pruning is the most important optimization to skip branches that cannot lead to a valid solution.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(2^T)$ where T is target value.
    - **Space Complexity:** $O(T)$ (recursion depth).

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you use Pruning or Bitmasking to significantly reduce the search space?
- **Scale Question:** How would you parallelize the search? Would you use Work Stealing to balance the load between threads?
- **Edge Case Probe:** What is the maximum depth of recursion before you hit a stack overflow?

## 🔗 Related Problems

- [Permutations](../permutations/PROBLEM.md) — Next in category
- [Subsets](../subsets/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
