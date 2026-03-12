#  🌳 Backtracking: Subsets II

## 📝 Description
[LeetCode 90](https://leetcode.com/problems/subsets-ii/)
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Duplicate Elements." Input `[1, 2, 2]` produces duplicates like `[1, 2]` (using the first 2) and `[1, 2]` (using the second 2). The naive power set algorithm fails.

**The Hero:** "The Sort & Skip." If we sort the array, duplicates are adjacent.

**The Plot:**

1. Sort `nums`: `[1, 2, 2]`.
2. Backtracking Logic:
   - **Pick:** Add `nums[i]`, recurse.
   - **No-Pick:** Skip `nums[i]`. BUT, also skip *all* subsequent copies of `nums[i]` (e.g., if we decide NOT to pick the first 2, we shouldn't pick the second 2 either, or we'll generate the same subsets).
3. Loop Condition: `while (i + 1 < n && nums[i] == nums[i+1]) i++;`

**The Twist (Failure):** **The Logic Gap.** Why skip all? Because the "Pick" branch of the *first* 2 already covered all combinations involving {2}. The "No-Pick" branch implies we want subsets *without* a 2 derived from this position.

**Interview Signal:** Handling **Duplicates in Combinatorics**.

## 🚀 Approach & Intuition
Sort array first. In the "exclude" step, skip all identical adjacent elements.

### C++ Pseudo-Code
```cpp
vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    vector<int> curr;
    
    function<void(int)> backtrack = [&](int i) {
        if (i == nums.size()) {
            res.push_back(curr);
            return;
        }
        
        // Include
        curr.push_back(nums[i]);
        backtrack(i + 1);
        curr.pop_back();
        
        // Exclude - skip duplicates
        while (i + 1 < nums.size() && nums[i] == nums[i+1]) i++;
        backtrack(i + 1);
    };
    
    backtrack(0);
    return res;
}
```

### Key Observations:

- Backtracking is essentially a DFS on a state-space tree where we 'undo' the last move to explore other branches.
- Pruning is the most important optimization to skip branches that cannot lead to a valid solution.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot 2^N)$
    - **Space Complexity:** $O(N)$

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

- [Combination Sum II](../combination_sum_ii/PROBLEM.md) — Next in category
- [Permutations](../permutations/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
