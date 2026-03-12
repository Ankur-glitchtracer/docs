#  🌲 Tree: Maximum Depth of Binary Tree

## 📝 Description
[LeetCode 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
Given the `root` of a binary tree, return its maximum depth.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Infinite Descent." Not knowing how deep a structure goes and risking a stack overflow if not handled with base cases.

**The Hero:** "The Bottom-Up Reporter." A recursive approach where each node reports the height of its tallest child back up to its parent.

**The Plot:**

1. Base Case: If node is `None`, its depth is 0.
2. Recursive Step: Get `max_depth` of left and right children.
3. Return `1 + max(left_depth, right_depth)`.

**The Twist (Failure):** **The Skewed Tree.** On a very deep, single-branch tree (like a linked list), recursion can hit the limit. Use an iterative BFS if the stack is constrained.

**Interview Signal:** Mastery of **Recursive DFS** and tree property calculation.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(H)$ (Tree height)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you solve this iteratively if you were worried about stack overflow from deep recursion?
- **Scale Question:** If the tree is a multi-terabyte B-Tree in a database, how do you optimize node traversal to minimize disk hits?
- **Edge Case Probe:** What if the tree is extremely skewed (effectively a linked list)? What if it's empty?

## 🔗 Related Problems

- [Diameter of Binary Tree](../diameter_of_binary_tree/PROBLEM.md) — Next in category
- [Invert Binary Tree](../invert_binary_tree/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
