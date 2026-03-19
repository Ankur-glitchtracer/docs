---
impact: "High"
nr: false
confidence: 5
---
# 🌳 Backtracking: Subsets

## 📝 Problem Description
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

!!! info "Real-World Application"
    - **Optimization:** Solving NP-complete problems (e.g., Knapsack).
    - **Test Case Generation:** Exhaustive combinatorial testing.
    - **Pattern Recognition:** Generating feature sets for machine learning models.

## 🛠️ Constraints & Edge Cases
- $1 \le nums.length \le 10$
- $-10 \le nums[i] \le 10$
- **Edge Cases to Watch:** 
    - Empty input array (return `[[]]`).
    - Arrays with a single element.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    For every element, you have two choices: **Include** it in the subset or **Exclude** it. This binary branching naturally forms a decision tree of height $N$, where all leaves are valid subsets.

### 🐢 Brute Force (Naive)
Generating all possible combinations using iterative loops is complex to manage. Backtracking provides a structured DFS approach that handles this naturally.

### 🐇 Optimal Approach
1. Define a recursive `backtrack(index)` function.
2. In each call, we make two decisions:
    - **Include** `nums[index]`: Append to current subset, move to `index + 1`, then pop.
    - **Exclude** `nums[index]`: Move to `index + 1` without modifying the subset.
3. Base case: When `index == len(nums)`, append a copy of the current subset to results.

### 🧩 Visual Tracing
```mermaid
graph TD
    Root(( )) -->|Include nums[0]| I[Include]
    Root -->|Exclude nums[0]| E[Exclude]
    I -->|Include nums[1]| II[Include, Include]
    I -->|Exclude nums[1]| IE[Include, Exclude]
    style Root fill:#f9f,stroke:#333
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N \cdot 2^N)$ — We generate $2^N$ subsets, and each takes $\mathcal{O}(N)$ to copy into the result.
- **Space Complexity:** $\mathcal{O}(N)$ — The depth of the recursion stack is $N$.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Use backtracking with pruning (e.g., `Subsets II` if duplicates are present).
- **Alternative Data Structures:** Bit manipulation is a highly efficient way to represent and generate subsets for small $N$ ($0$ to $2^N-1$).

## 🔗 Related Problems
- [Combination Sum](../combination_sum/PROBLEM.md) — Fundamental backtracking.
- [Permutations](../permutations/PROBLEM.md) — Variation with order significance.
- [Subsets II](../subsets_ii/PROBLEM.md) — Handling duplicate elements.
