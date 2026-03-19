---
impact: "Medium"
nr: false
confidence: 4
---
# 🪜 Greedy: Jump Game

## 📝 Problem Description
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return `true` if you can reach the last index, or `false` otherwise.

!!! info "Real-World Application"
    This algorithm is essential for pathfinding and decision trees, where you need to check if a valid path exists in a state space given constrained movement.

## 🛠️ Constraints & Edge Cases
- $1 \le nums.length \le 10^4$
- $0 \le nums[i] \le 10^5$
- **Edge Cases:** Single element array, unreachable last index.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Instead of trying every possible jump from the start, work backwards from the last index. If you can reach the `goal` from a previous index, update the `goal` to that index.

### 🐢 Brute Force (Naive)
Dynamic programming, checking all possible jump combinations: $O(N^2)$.

### 🐇 Optimal Approach
1. Set `goal` to the last index.
2. Iterate backwards from `len(nums) - 2` to `0`.
3. If current index + jump capacity $\ge$ `goal`, update `goal = current_index`.
4. If `goal == 0` at the end, return `true`.

### 🧩 Visual Tracing
```mermaid
graph LR
    A[Start: 0] --> B[Jump 2]
    B --> C[Jump 1]
    C --> D[Goal: Last index]
    style D fill:#f9f,stroke:#333
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ — Single pass through the array.
- **Space Complexity:** $\mathcal{O}(1)$ — No extra space used.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Return the minimum number of jumps to reach the end (Jump Game II).
- **Alternative Data Structures:** DP can solve this but is slower.

## 🔗 Related Problems
- [Jump Game II](../jump_game_ii/PROBLEM.md)
