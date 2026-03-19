---
impact: "Medium"
nr: false
confidence: 2
---
# 🔽 Stack: Min Stack

## 📝 Description
[LeetCode 155](https://leetcode.com/problems/min-stack/)
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

!!! info "Real-World Application"
    Useful in systems where you need to track state history with snapshot capabilities, such as **Undo/Redo** features in text editors where you might want to know the "min" or "max" property of the state at any point in history without scanning.

## 🛠️ Constraints & Edge Cases
- $-2^{31} \le \text{val} \le 2^{31} - 1$
- Methods `pop`, `top`, and `getMin` operations will always be called on non-empty stacks.
- **Edge Cases to Watch:**
    - Duplicate minimum values (need to ensure popping one doesn't lose the record of the other).
    - Empty stack operations (though constraints say otherwise, good to clarify).

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    A single variable `min_val` isn't enough because when we pop the minimum, we forget what the *previous* minimum was. We need to store the history of minimums. We can use a **second stack** that stays in sync with the main stack.

### 🐢 Brute Force (Naive)
Use a standard list. `getMin()` iterates the list to find the minimum.
- **Time Complexity:** $O(N)$ for `getMin()`.

### 🐇 Optimal Approach
1.  **Main Stack:** Stores all values normally.
2.  **Min Stack:** Stores the minimum value seen *so far*.
3.  **Push(val):**
    - Push to `Main`.
    - Push `min(val, MinStack.top)` to `MinStack` (or only push if `val <= MinStack.top`).
4.  **Pop():**
    - Pop `Main`.
    - If popped value matches `MinStack.top`, Pop `MinStack`.

### 🧩 Visual Tracing
```mermaid
graph TD
    A[Push -2] -->|Main: [-2], Min: [-2]| B
    B[Push 0] -->|Main: [-2, 0], Min: [-2]| C
    C[Push -3] -->|Main: [-2, 0, -3], Min: [-2, -3]| D
    D[Pop] -->|Main: [-2, 0], Min: [-2]| E
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(1)$ — All operations are constant time.
- **Space Complexity:** $\mathcal{O}(N)$ — We store an auxiliary stack.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Implement `MaxStack`. Implement `MinStack` with $O(1)$ extra space (using encoded values: `val = 2*x - min`).
- **Optimization:** Only push to `MinStack` if the new value is $\le$ current min to save space on average.

## 🔗 Related Problems
- [Evaluate RPN](../evaluate_reverse_polish_notation/PROBLEM.md) — Next in category
- [Sliding Window Maximum](../../03_sliding_window/sliding_window_maximum/PROBLEM.md) — Related concept
