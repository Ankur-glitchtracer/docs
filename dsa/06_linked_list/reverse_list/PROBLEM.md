#  🔄 Linked List: Reverse Linked List

## 📝 Description
[LeetCode 206](https://leetcode.com/problems/reverse-linked-list/)
Given the `head` of a singly linked list, reverse the list and return its new head.

## 🛠️ Requirements/Constraints

- The number of nodes in the list is the range $[0, 5000]$.
- $-5000 \le Node.val \le 5000$

## 🧠 The Engineering Story

**The Villain:** "The Memory Leak." Trying to reverse a list by creating new nodes, which doubles memory usage ($O(N)$ space). Or, losing the "rest of the list" because you flipped a pointer too early.

**The Hero:** "The Three-Pointer Flip." A constant-space ($O(1)$) approach using `prev`, `curr`, and `next` pointers to reverse the list in-place.

**The Plot:**

1. Save `curr.next` to avoid losing the rest of the chain.
2. Flip `curr.next` to point to `prev`.
3. Advance `prev` and `curr` one step forward.

**The Twist (Failure):** **The Head Loss.** Forgetting to return `prev` as the new head, leaving the client stuck with a pointer to the now-final node.

**Interview Signal:** Mastery of **In-place Pointer Manipulation** and Linked List mechanics.

## 🚀 Approach & Intuition
Reversing a linked list is about reorienting the pointers. Instead of creating a new list, we can flip the `next` pointer of each node to point to its predecessor. We need three pointers to do this safely: `prev`, `curr`, and a temporary `next_node`.

### Key Observations:

- We must store the `next` node before overwriting `curr.next`.
- The `head` of the reversed list will be the last node of the original list.
- After the loop, `prev` will point to the new head.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the linked list. We visit each node exactly once.
    - **Space Complexity:** $O(1)$ as we only use a few pointers to track the state.

## 💻 Solution Implementation

```python
--8<-- "dsa/06_linked_list/reverse_list/solution.py"
```

!!! success "Aha! Moment"
    The "magic" happens when you realize you don't need to move the nodes—just the links between them. By keeping a reference to the previous node, you can point backwards as you move forwards.

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you reverse only a sub-portion of the list from position $M$ to $N$? Can you reverse it in groups of size $K$?
- **Scale Question:** If the list is too large to fit in memory and is stored as a series of blocks on disk, how do you reverse the pointers efficiently?
- **Edge Case Probe:** How does your solution handle an empty list or a list with only one node?

## 🔗 Related Problems

- [Merge Two Sorted Lists](../merge_sorted_lists/PROBLEM.md) — Next in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
