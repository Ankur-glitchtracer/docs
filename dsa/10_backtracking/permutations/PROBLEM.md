---
impact: "Medium"
nr: false
confidence: 2
---
# 🔄 Backtracking: Permutations

## 📝 Description
[LeetCode 46](https://leetcode.com/problems/permutations/)
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

!!! info "Real-World Application"
    Used in **Traveling Salesman Problem** (generating all routes), **Job Scheduling** (all orderings of tasks), and testing all interaction sequences in a system.

## 🛠️ Constraints & Edge Cases
- $1 \le nums.length \le 6$
- Distinct integers.
- **Edge Cases to Watch:**
    - `n=1`: `[[1]]`.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    A permutation is an ordering. For the first position, we can pick any of the $N$ numbers. For the second, we can pick any of the remaining $N-1$, and so on. We can simulate this selection process by recursively picking a number, marking it as "used" (or removing it from available choices), and recurring.

### 🐢 Brute Force (Naive)
Same as optimal. This is an exhaustive search problem.

### 🐇 Optimal Approach
1.  **Base Case:** If `len(current_perm) == len(nums)`, add to results.
2.  **Loop:** Iterate through `nums`.
3.  **Check:** If number is already in `current_perm` (or marked used), skip.
4.  **Recurse:** Add number, recurse, remove number (backtrack).

### 🧩 Visual Tracing
```mermaid
graph TD
    Root[[]] -->|1| A[1]
    Root -->|2| B[2]
    A -->|2| C[1,2]
    A -->|3| D[1,3]
    B -->|1| E[2,1]
    B -->|3| F[2,3]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N \cdot N!)$ — There are $N!$ permutations, and each takes $O(N)$ to build/copy.
- **Space Complexity:** $\mathcal{O}(N)$ — Recursion stack.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Permutations II (Inputs contain duplicates). Logic requires sorting and skipping duplicates (similar to Combination Sum II).
- **Alternative:** Heap's Algorithm (swapping elements in place).

## 🔗 Related Problems
- [Permutations II](https://leetcode.com/problems/permutations-ii/) — With duplicates
- [Combination Sum](../combination_sum/PROBLEM.md) — Selection without order
