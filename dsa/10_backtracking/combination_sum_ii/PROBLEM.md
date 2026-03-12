#  🎯 Backtracking: Combination Sum II

## 📝 Description
[LeetCode 40](https://leetcode.com/problems/combination-sum-ii/)
Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination. The solution set must not contain duplicate combinations.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Finite Duplicates." Unlike Combination Sum I, you can't reuse numbers. Unlike Subsets, you have a target sum. Input `(To be detailed...)`, Target `8`. Duplicates (`1, 1`) exist but each can be used once.

**The Hero:** "The Sorted Loop." Sort the candidates to group duplicates. Iterate through options.

**The Plot:**

1. Sort `candidates`.
2. Iterate `i` from `start` to `end`.
3. If `i > start` and `candidates[i] == candidates[i-1]`: Continue (Skip duplicates at the same tree level).
4. If `candidates[i] > target`: Break (Sorted array, no hope for future elements).
5. Pick `candidates[i]`, recurse with `target - val` and `i + 1`.
6. Backtrack.

**The Twist (Failure):** **The Loop vs Recursion.** We use a `for` loop inside the recursion to try different starting numbers for the current slot. `i > start` ensures we allow `1, 1` (different levels) but not `1` (same level skipping).

**Interview Signal:** Advanced **Duplicate Handling** in constraints.

## 🚀 Approach & Intuition
Use a loop inside recursion to manage branches, skipping duplicates.

### C++ Pseudo-Code
```cpp
vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> res;
    vector<int> curr;
    
    function<void(int, int)> backtrack = [&](int start, int remain) {
        if (remain == 0) {
            res.push_back(curr);
            return;
        }
        for (int i = start; i < candidates.size(); i++) {
            if (i > start && candidates[i] == candidates[i-1]) continue;
            if (candidates[i] > remain) break;
            
            curr.push_back(candidates[i]);
            backtrack(i + 1, remain - candidates[i]);
            curr.pop_back();
        }
    };
    
    backtrack(0, target);
    return res;
}
```

### Key Observations:

- Backtracking is essentially a DFS on a state-space tree where we 'undo' the last move to explore other branches.
- Pruning is the most important optimization to skip branches that cannot lead to a valid solution.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(2^N)$
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

- [Word Search](../word_search/PROBLEM.md) — Next in category
- [Subsets II](../subsets_ii/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
