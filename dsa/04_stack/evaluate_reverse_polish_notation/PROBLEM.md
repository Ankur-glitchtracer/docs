#  🧮 Stack: Evaluate Reverse Polish Notation

## 📝 Description
[LeetCode 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Note that division between two integers should truncate toward zero.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- Constraints vary depending on the specific stack application.

## 🧠 The Engineering Story

**The Villain:** "The Order of Operations." Parsing `(3 + 4) * 5` is hard because you have to wait for the inner parenthesis. Infix notation requires complex precedence rules.

**The Hero:** "The Postfix Stack." In RPN (`3 4 + 5 *`), the operator always comes *after* its operands. We never need parentheses.

**The Plot:**

1. Iterate through tokens.
2. If it's a number, push to stack.
3. If it's an operator (`+`, `-`, `*`, `/`), pop the top two numbers.
4. Perform the operation and push the result back.
5. The final answer is the only item left in the stack.

**The Twist (Failure):** **The Subtraction Order.** `a - b` is not `b - a`. When you pop, the *first* popped item is the right operand (`b`), and the *second* is the left (`a`).

**Interview Signal:** Understanding of **Expression Evaluation** and stack mechanics.

## 🚀 Approach & Intuition
Push numbers, pop for operators.

### C++ Pseudo-Code
```cpp
int evalRPN(vector<string>& tokens) {
    stack<int> s;
    for (string& t : tokens) {
        if (t == "+" || t == "-" || t == "*" || t == "/") {
            int b = s.top(); s.pop();
            int a = s.top(); s.pop();
            if (t == "+") s.push(a + b);
            else if (t == "-") s.push(a - b);
            else if (t == "*") s.push(a * b);
            else s.push(a / b);
        } else {
            s.push(stoi(t));
        }
    }
    return s.top();
}
```

### Key Observations:

- Stacks are essential for problems involving nested structures, like parentheses or expression evaluation.
- Monotonic stacks are a powerful variation used to find the next greater or smaller element in $O(N)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(N)$

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

- [Generate Parentheses](../generate_parentheses/PROBLEM.md) — Next in category
- [Min Stack](../min_stack/PROBLEM.md) — Previous in category
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
