#  🔽 Stack: Min Stack

## 📝 Description
[LeetCode 155](https://leetcode.com/problems/min-stack/)
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- Constraints vary depending on the specific stack application.

## 🧠 The Engineering Story

**The Villain:** "The Linear Scan." Finding the minimum element in a standard stack takes $O(N)$ because you have to pop everything off to check.

**The Hero:** "The Parallel Stack." Keep a secondary stack that tracks the "minimum so far" at every level of the main stack.

**The Plot:**

1. Push to `main_stack` normally.
2. For `min_stack`, push `min(val, min_stack.top())`.
3. When popping, pop from both.
4. `getMin()` simply returns `min_stack.top()`.

**The Twist (Failure):** **The Empty Check.** Trying to access `min_stack.top()` on the very first push when it's empty. Initialize with infinity or handle the base case.

**Interview Signal:** Mastery of **State Tracking** alongside data structure operations.

## 🚀 Approach & Intuition
Use a second stack to keep track of the minimum value at each depth.

### C++ Pseudo-Code
```cpp
class MinStack {
    stack<int> s;
    stack<int> minS;
public:
    void push(int val) {
        s.push(val);
        if (minS.empty() || val <= minS.top()) minS.push(val);
    }
    
    void pop() {
        if (s.top() == minS.top()) minS.pop();
        s.pop();
    }
    
    int top() { return s.top(); }
    int getMin() { return minS.top(); }
};
```

### Key Observations:

- Stacks are essential for problems involving nested structures, like parentheses or expression evaluation.
- Monotonic stacks are a powerful variation used to find the next greater or smaller element in $O(N)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(1)$ for all operations.
    - **Space Complexity:** $O(N)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you implement a 'Max Stack'? Can you implement a stack where `popMin()` runs in $O(\log N)$ or $O(1)$?
- **Scale Question:** If the stack grows to millions of elements, how would you persist it to disk while keeping the $O(1)$ property for `getMin()`?
- **Edge Case Probe:** What should the behavior be when calling `getMin()` or `top()` on an empty stack?

## 🔗 Related Problems

- [Evaluate RPN](../evaluate_reverse_polish_notation/PROBLEM.md) — Next in category
- [Valid Parentheses](../valid_parentheses/PROBLEM.md) — Previous in category
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
