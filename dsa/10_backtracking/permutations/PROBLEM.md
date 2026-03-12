#  🔄 Backtracking: Permutations

## 📝 Description
[LeetCode 46](https://leetcode.com/problems/permutations/)
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Order Obsession." Generating all possible arrangements of a set. For $N=10$, there are $10! = 3.6M$ arrangements. Simple loops can't handle dynamic depths.

**The Hero:** "The Decision Tree Explorer." A recursive function that swaps elements to build every possible order, then swaps them back (backtracks) to try the next path.

**The Plot:**

1. Base Case: If `current_path` length == `nums` length, you found a permutation.
2. Recursive Step: Loop through all numbers.
3. If number not in `current_path`:
   - Add to path.
   - Recurse.
   - Remove from path (The "Backtrack").

**The Twist (Failure):** **The Duplicate Dilemma.** If the input has duplicate numbers, this simple check fails. You need to sort and use a "used" array to avoid redundant paths.

**Interview Signal:** Mastery of **State-Space Search** and recursion cleanup.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- Backtracking is essentially a DFS on a state-space tree where we 'undo' the last move to explore other branches.
- Pruning is the most important optimization to skip branches that cannot lead to a valid solution.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N 	imes N!)$
    - **Space Complexity:** $O(N 	imes N!)$

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

- [Subsets II](../subsets_ii/PROBLEM.md) — Next in category
- [Combination Sum](../combination_sum/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
