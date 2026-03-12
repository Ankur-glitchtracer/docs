#  🏎️ Linked Lists: Linked List Cycle

## 📝 Description
[LeetCode 141](https://leetcode.com/problems/linked-list-cycle/)
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Infinite Loop." Traversing a list that has a cycle will hang your program and crash the system.

**The Hero:** "The Tortoise and the Hare." Two pointers moving at different speeds. If there's a cycle, the fast one will eventually lap the slow one.

**The Plot:**

1. Initialize `slow` and `fast` at the head.
2. Move `slow` by 1 step and `fast` by 2 steps.
3. If they ever point to the same node, a cycle exists.
4. If `fast` reaches `None`, there is no cycle.

**The Twist (Failure):** **The Null Pointer.** Forgetting to check `fast.next` before moving `fast` 2 steps, leading to a crash on short lists.

**Interview Signal:** Mastery of **Relative Velocity** and Floyd's Cycle-Finding Algorithm.

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

- **Harder Variant:** Can you find the exact node where the cycle begins (Linked List Cycle II / Floyd's Cycle-Finding Algorithm)?
- **Scale Question:** If the linked list is distributed across multiple nodes in a network (each node points to a URI), how would you detect a cycle?
- **Edge Case Probe:** How does your code handle a single node that points to itself? What about a list with no cycle?

## 🔗 Related Problems

- [Find the Duplicate Number](../find_the_duplicate_number/PROBLEM.md) — Next in category
- [Add Two Numbers](../add_two_numbers/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
