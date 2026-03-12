#  ⚖️ Stacks: Valid Parentheses

## 📝 Description
[LeetCode 20](https://leetcode.com/problems/valid-parentheses/)
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

## 🛠️ Requirements/Constraints

- $1 <= s.length <= 10^4$
- `s` consists of parentheses only '()[]{}'.

## 🧠 The Engineering Story

**The Villain:** "The Nested Mess." A string like `({[ ]})` where you need to ensure every opening tag has a matching closing tag in the correct order. Using `count()` fails because `([)]` is invalid but counts are equal.

**The Hero:** "The LIFO Stack." Store every opener. When you see a closer, it MUST match the most recent opener.

**The Plot:**

1. Create a map of closers to openers: `match = {')': '(', '}': '{', ']': '['}`.
2. Iterate through the string.
3. If it's an opener, push to `stack`.
4. If it's a closer:
   - Pop from stack.
   - If stack is empty or popped item doesn't match, return `False`.
5. Finally, return `len(stack) == 0`.

**The Twist (Failure):** **The Early Closer.** A string starting with `)` will cause an error if you try to pop from an empty stack.

**Interview Signal:** Mastery of **LIFO (Last-In-First-Out)** logic and data structure selection.

## 🚀 Approach & Intuition
A stack is the natural choice for problems involving nested structures. As we encounter opening brackets, we "buffer" them. A closing bracket must match the most recently seen opening bracket, which is exactly what a stack's `pop()` operation provides.

### Key Observations:

- A closing bracket is only valid if the stack is not empty and matches the top.
- The final stack must be empty for the entire string to be valid (no unclosed openers).
- Using a hash map for bracket pairs makes the code cleaner and easier to extend.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ - We process each character exactly once.
    - **Space Complexity:** $O(N)$ - In the worst case (all openers), we store all characters in the stack.

## 💻 Solution Implementation

```python
--8<-- "dsa/04_stack/valid_parentheses/solution.py"
```

!!! success "Aha! Moment"
    The "LIFO" nature of the stack perfectly mirrors the "Last Opened, First Closed" requirement of balanced parentheses.

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you find the length of the longest valid parentheses substring? What if there are multiple types of delimiters with priority?
- **Scale Question:** If you are linting a 1GB source file, how can you check for balanced brackets using a memory-mapped file?
- **Edge Case Probe:** How does the stack-based approach handle a string that only contains closing brackets?

## 🔗 Related Problems

- [Min Stack](../min_stack/PROBLEM.md) — Next in category
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
