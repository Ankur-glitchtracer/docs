#  ↔️ Linked Lists: Palindrome Linked List

## 📝 Description
[LeetCode 234](https://leetcode.com/problems/palindrome-linked-list/)
Given the `head` of a singly linked list, return `true` if it is a palindrome.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Memory Double." Copying the list into an array to check for a palindrome ($O(N)$ space).

**The Hero:** "The Half-Flip." Find the middle, reverse the second half, and compare it to the first.

**The Plot:**

1. Use **Fast/Slow** pointers to find the middle.
2. **Reverse** the second half of the list in-place.
3. Compare the first half and the reversed second half node by node.

**The Twist (Failure):** **The Permanent Damage.** Leaving the list reversed, which might break other parts of the application that expect the original structure. (Best practice: reverse it back).

**Interview Signal:** Mastery of **Algorithm Composition** (Combining Middle-Finding, Reversing, and Comparison).

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- Always consider using a dummy head node to simplify edge cases like inserting at the head or deleting the only node.
- Fast and slow pointers are a common pattern for finding the middle or detecting cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the input is sorted or has a limited range? Can you optimize space from $O(N)$ to $O(1)$?
- **Scale Question:** If the dataset is too large to fit in RAM, how would you use external sorting or a distributed hash table?
- **Edge Case Probe:** How does your solution handle duplicates, empty inputs, or extremely large integers?

## 🔗 Related Problems

- `[Related Problem 1](../category/problem_name/PROBLEM.md)` — (To be detailed...)
- `[Related Problem 2](../category/problem_name/PROBLEM.md)` — (To be detailed...)
