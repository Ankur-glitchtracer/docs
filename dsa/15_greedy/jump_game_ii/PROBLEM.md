---
impact: "High"
nr: false
confidence: 4
---
# 🪜 Greedy: Jump Game II

## 📝 Problem Description
Given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`. Each element `nums[i]` represents the maximum jump length from index `i`. Return the minimum number of jumps to reach `nums[n - 1]`.

!!! info "Real-World Application"
    Used in optimization problems to find the fastest path between states, like resource scheduling with a limited capacity per step.

## 🛠️ Constraints & Edge Cases
- $1 \le nums.length \le 10^4$
- **Edge Cases:** Single element array, last index already reachable.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Use a BFS-like approach with a sliding window. At each step, find the range of indices reachable with the next jump. The next jump will be the farthest possible reach from the current window.

### 🐢 Brute Force (Naive)
BFS to find the shortest path, potentially $O(N^2)$.

### 🐇 Optimal Approach
1. Maintain a window `[l, r]` representing current reach.
2. For each window, find the max reach for the next window.
3. Once we exceed the current right boundary, update boundary and increment jumps.

### 🧩 Visual Tracing
```mermaid
graph LR
    A[Window] -->|Jump| B[Next Window]
    B -->|Jump| C[Goal]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ — Each index is visited once.
- **Space Complexity:** $\mathcal{O}(1)$ — No extra storage.

---

## 🎤 Interview Toolkit

- **Harder Variant:** What if you need to return the actual path?

## 🔗 Related Problems
- [Jump Game](../jump_game/PROBLEM.md)
