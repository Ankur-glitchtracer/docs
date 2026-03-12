#  🌲 Tree: Lowest Common Ancestor of a Binary Search Tree

## 📝 Description
[LeetCode 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Blind Search." Searching the entire tree for `p` and `q` ($O(N)$). We are ignoring the BST property!

**The Hero:** "The BST Split." In a BST, the LCA is the node where `p` and `q` split ways (one is smaller, one is larger).

**The Plot:**

1. Start at `root`.
2. If `p.val < root.val` and `q.val < root.val`: Both are in the left subtree. Move left.
3. If `p.val > root.val` and `q.val > root.val`: Both are in the right subtree. Move right.
4. Else: We found the split point (or one of them is the root). This is the LCA.

**The Twist (Failure):** **General Binary Tree.** This logic only works for BSTs. For general trees, you need post-order traversal to bubble up existence.

**Interview Signal:** Leveraging **BST Properties** for $O(\log N)$ optimization.

## 🚀 Approach & Intuition
Utilize value comparisons to find split point.

### C++ Pseudo-Code
```cpp
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    while (root) {
        if (p->val < root->val && q->val < root->val)
            root = root->left;
        else if (p->val > root->val && q->val > root->val)
            root = root->right;
        else
            return root;
    }
    return nullptr;
}
```

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(H)$ (Height of tree, $\log N$ if balanced)
    - **Space Complexity:** $O(1)$ (Iterative)

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

- [Level Order Traversal](../binary_tree_level_order_traversal/PROBLEM.md) — Next in category
- [Subtree of Another Tree](../subtree_of_another_tree/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
