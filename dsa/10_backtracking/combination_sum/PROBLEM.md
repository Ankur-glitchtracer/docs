---
impact: "Medium"
nr: false
confidence: 2
---
# 🎯 Backtracking: Combination Sum

## 📝 Description
[LeetCode 39](https://leetcode.com/problems/combination-sum/)
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order. The same number may be chosen from `candidates` an unlimited number of times.

!!! info "Real-World Application"
    This is the **Unbounded Knapsack Problem**. It's used in **Coin Change** (making change for a dollar using specific denominations) or resource allocation where you can use multiple instances of the same resource type.

## 🛠️ Constraints & Edge Cases
- $1 \le \text{candidates.length} \le 30$
- $1 \le \text{target} \le 500$
- **Edge Cases to Watch:**
    - Target cannot be reached.
    - Candidates are larger than target.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    We need to make a series of decisions: "Do I take this number, or do I skip it?" Since we can reuse numbers, if we decide to *take* a number, we stay at the same index for the next recursion. If we *skip*, we move to the next index. This forms a decision tree.

### 🐢 Brute Force (Naive)
Try every possible combination of every length. Without pruning (stopping when sum > target), this would be infinite.

### 🐇 Optimal Approach (DFS)
1.  Define `backtrack(i, current_sum, current_list)`.
2.  **Base Case:** If `current_sum == target`, add copy of `current_list` to result.
3.  **Base Case:** If `current_sum > target` OR `i >= len(candidates)`, return.
4.  **Branch 1 (Include):**
    - Add `candidates[i]` to list.
    - Recurse with `(i, current_sum + candidates[i])` -> *Note: index `i` stays same*.
    - Backtrack (pop from list).
5.  **Branch 2 (Exclude):**
    - Recurse with `(i + 1, current_sum)`.

### 🧩 Visual Tracing
```mermaid
graph TD
    Root["Start: t=7"]

    Root -->|+2| A["t=5 | [2]"]
    A -->|+2| B["t=3 | [2,2]"]
    B -->|+2| C["t=1 | [2,2,2]"]
    C -->|+2| X1["t=-1 ✗"]
    C -->|+3| X2["t=-2 ✗"]

    B -->|+3| D["t=0 ✓ [2,2,3]"]
    B -->|+6| X3["t=-3 ✗"]

    A -->|+3| E["t=2 | [2,3]"]
    E -->|+2| F["t=0 ✓ [2,3,2]"]
    E -->|+3| X4["t=-1 ✗"]

    A -->|+6| X5["t=-1 ✗"]

    Root -->|+3| G["t=4 | [3]"]
    G -->|+3| H["t=1 | [3,3]"]
    H -->|+3| X6["t=-2 ✗"]

    Root -->|+6| I["t=1 | [6]"]
    I -->|+6| X7["t=-5 ✗"]

    Root -->|+7| J["t=0 ✓ [7]"]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(2^T)$ — Roughly exponential based on Target/MinCandidate.
- **Space Complexity:** $\mathcal{O}(T)$ — Max depth of recursion (e.g., if we pick 1 repeated T times).

---

## 🎤 Interview Toolkit

- **Harder Variant:** Combination Sum II (No duplicates allowed).
- **Optimization:** Sort candidates and break loop early if `current_sum + candidates[i] > target`.

## 🔗 Related Problems
- [Combination Sum II](../combination_sum_ii/PROBLEM.md) — Next in category
- [Permutations](../permutations/PROBLEM.md) — Previous in category
