#  🌲 Tree: Same Tree

## 📝 Description
[LeetCode 100](https://leetcode.com/problems/same-tree/)
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Structural Mimic." Two trees might have the same values but different structures (e.g., `1->2` vs `1->null->2`).

**The Hero:** "The Simultaneous Traversal." Traverse both trees at the exact same time.

**The Plot:**

1. Base Cases:
   - If both `p` and `q` are `None`: True.
   - If one is `None` (but not both): False.
   - If `p.val != q.val`: False.
2. Recursion: Return `isSame(p.left, q.left) && isSame(p.right, q.right)`.

**The Twist (Failure):** **Null Pointer Exceptions.** Forgetting the "one is None" check before accessing `val`.

**Interview Signal:** Mastery of **Recursive Comparisons**.

## 🚀 Approach & Intuition
Check structure and values simultaneously.

### C++ Pseudo-Code
```cpp
bool isSameTree(TreeNode* p, TreeNode* q) {
    if (!p && !q) return true;
    if (!p || !q || p->val != q->val) return false;
    return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}
```

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(H)$

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

- [Subtree of Another Tree](../subtree_of_another_tree/PROBLEM.md) — Next in category
- [Balanced Binary Tree](../balanced_binary_tree/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
