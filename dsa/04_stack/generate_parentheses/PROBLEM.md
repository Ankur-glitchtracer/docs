#  🎭 Stack: Generate Parentheses

## 📝 Description
[LeetCode 22](https://leetcode.com/problems/generate-parentheses/)
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- Constraints vary depending on the specific stack application.

## 🧠 The Engineering Story

**The Villain:** "The Invalid Combo." Generating all $2^{2N}$ combinations of `(` and `)` and checking if they are valid. Efficient for $N=3$, impossible for $N=20$.

**The Hero:** "The Backtracking Pruner." Only add a parenthesis if it could possibly lead to a valid solution.

**The Plot:**

1. Track `open_count` and `close_count`.
2. If `open_count < n`: We can add `(`.
3. If `close_count < open_count`: We can add `)`.
4. If `open_count == close_count == n`: Valid string found. Add to results.

**The Twist (Failure):** **The Order.** You can't add `)` if `close >= open`. That's the only rule you need to prevent `)(`.

**Interview Signal:** Mastery of **Constrained Backtracking**.

## 🚀 Approach & Intuition
Recursively build strings, respecting valid parenthesis rules.

### C++ Pseudo-Code
```cpp
vector<string> generateParenthesis(int n) {
    vector<string> res;
    function<void(string, int, int)> backtrack = 
        [&](string s, int open, int close) {
        if (s.length() == 2 * n) {
            res.push_back(s);
            return;
        }
        if (open < n) backtrack(s + "(", open + 1, close);
        if (close < open) backtrack(s + ")", open, close + 1);
    };
    backtrack("", 0, 0);
    return res;
}
```

### Key Observations:

- Stacks are essential for problems involving nested structures, like parentheses or expression evaluation.
- Monotonic stacks are a powerful variation used to find the next greater or smaller element in $O(N)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(4^N / \sqrt{N})$ (Catalan number)
    - **Space Complexity:** $O(N)$ (Recursion depth)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you solve this using a single pass or by transforming the problem into a Monotonic Stack problem?
- **Scale Question:** If the stack needs to be persistent (undo/redo functionality), how would you implement it using a functional data structure?
- **Edge Case Probe:** What happens on an empty stack or when the input contains unexpected characters?

## 🔗 Related Problems

- [Daily Temperatures](../daily_temperatures/PROBLEM.md) — Next in category
- [Evaluate RPN](../evaluate_reverse_polish_notation/PROBLEM.md) — Previous in category
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
