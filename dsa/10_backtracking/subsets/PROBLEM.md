#  🌳 Backtracking: Subsets

## 📝 Description
[LeetCode 78](https://leetcode.com/problems/subsets/)
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Binary Switch." You have `N` items. For each item, you have exactly two choices: Include it or Exclude it. Standard loops can't handle this $2^N$ branching factor easily.

**The Hero:** "The Power Set Explorer." A recursive function that explores both branches for every element.

**The Plot:**

1. Base Case: If `index == nums.length`, add current `subset` to results.
2. **Branch 1 (Include):** Add `nums[index]` to `subset`, recurse `index + 1`, then pop (backtrack).
3. **Branch 2 (Exclude):** Skip `nums[index]`, recurse `index + 1`.

**The Twist (Failure):** **The Mutable List.** In Python/Java, if you add `subset` directly to the results list, you're adding a reference. When you backtrack, you modify the result! You must add a *copy* (e.g., `new ArrayList(subset)`).

**Interview Signal:** Mastery of **Pick/No-Pick** logic.

## 🚀 Approach & Intuition
Explore inclusion and exclusion for each element.

### C++ Pseudo-Code
```cpp
vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> res;
    vector<int> curr;
    function<void(int)> backtrack = [&](int i) {
        if (i == nums.size()) {
            res.push_back(curr);
            return;
        }
        // Include nums[i]
        curr.push_back(nums[i]);
        backtrack(i + 1);
        curr.pop_back();
        
        // Exclude nums[i]
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
    - **Space Complexity:** $O(N)$ (recursion stack)

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

- [Combination Sum](../combination_sum/PROBLEM.md) — Next in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite: Trees
