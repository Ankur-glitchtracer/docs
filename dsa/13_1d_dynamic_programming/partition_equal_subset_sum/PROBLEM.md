---
impact: "Medium"
nr: false
confidence: 4
---
# ⚖️ DP: Partition Equal Subset Sum

## 📝 Problem Description
Given a non-empty array `nums` containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

!!! info "Real-World Application"
    A variation of the **0/1 Knapsack Problem**, which is used in resource allocation, load balancing in distributed systems, and bin packing problems.

## 🛠️ Constraints & Edge Cases
- $1 \le \text{nums.length} \le 200$
- $1 \le \text{nums}[i] \le 100$
- **Edge Cases:** Total sum is odd (cannot partition), single element array.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    If the total sum is odd, it's impossible. If even, we need to find if any subset sums up to `Total / 2`. This reduces the problem to the standard **Subset Sum Problem**, a classic variation of the 0/1 Knapsack Problem.

### 🐢 Brute Force (Naive)
Generate all possible subsets and check their sums. There are $2^N$ subsets. For $N=200$, this is impossible.

### 🐇 Optimal Approach
Use a set to track all possible sums reachable using the elements seen so far:
1. Calculate `total_sum`. If odd, return `False`.
2. `target = total_sum / 2`.
3. Iterate through `nums`, maintaining a set of all reachable sums $\le target$.
4. If `target` is ever reached, return `True`.

### 🧩 Visual Tracing
```mermaid
graph TD
    S[Start: {0}] -- num: 1 --> A[{0, 1}]
    A -- num: 5 --> B[{0, 1, 5, 6}]
    B -- num: 11 --> C[{0, 1, 5, 6, 11, 12, 16, 17}]
    style C fill:#ccf,stroke:#333,stroke-width:2px
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N \cdot S)$, where $S$ is the `target` sum. In the worst case, the number of reachable sums is bounded by $S$.
- **Space Complexity:** $\mathcal{O}(S)$ — The set of reachable sums will not exceed `target`.

---

## 🎤 Interview Toolkit

- **Harder Variant:** What if you need to partition into $k$ subsets with equal sum? (This is a much harder problem: Partition Problem, generally NP-Complete).
- **Alternative Data Structures:** For extremely dense subsets, a boolean array `dp[target + 1]` can be faster than a `set` due to cache locality.

## 🔗 Related Problems
- [Subsets](../../10_backtracking/subsets/PROBLEM.md) — Fundamental backtracking problem.
