#  🔀 Linked Lists: Merge Two Sorted Lists

## 📝 Description
[LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/)
Merge two sorted linked lists and return it as a sorted list.

## 🛠️ Requirements/Constraints

- The number of nodes in both lists is in the range $[0, 50]$.
- $-100 \le Node.val \le 100$
- Both lists are sorted in non-decreasing order.

## 🧠 The Engineering Story

**The Villain:** "The Complex Head Logic." Writing special `if` cases for the first node, the middle nodes, and the remaining nodes, leading to messy, buggy code.

**The Hero:** "The Dummy Head." Create a fake starting node so you can treat the first "real" node just like any other node.

**The Plot:**

1. Create a `dummy` node and a `curr` pointer.
2. Compare the heads of both lists.
3. Attach the smaller node to `curr.next` and move its head forward.
4. Repeat until one list is empty.
5. Attach the remainder of the non-empty list.

**The Twist (Failure):** **The Lost Tail.** Forgetting to attach the rest of the list once one side runs out.

**Interview Signal:** Mastery of **Pointer Re-linking** and clean structural code.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- A dummy head node simplifies the logic by providing a starting point for the merged list.
- The process is similar to the 'merge' step in Merge Sort, comparing heads of both lists and picking the smaller one.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N + M)$
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you merge $K$ sorted linked lists? (Use a Min-Heap).
- **Scale Question:** If these lists represent sorted logs from different servers, how would you merge them into a single stream in real-time?
- **Edge Case Probe:** What if one list is significantly longer than the other (e.g., 1 node vs 1 million nodes)?

## 🔗 Related Problems

- [Reorder List](../reorder_list/PROBLEM.md) — Next in category
- [Reverse Linked List](../reverse_list/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
