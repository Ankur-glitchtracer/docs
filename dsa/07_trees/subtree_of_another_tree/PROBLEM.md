#  🌲 Tree: Subtree of Another Tree

## 📝 Description
[LeetCode 572](https://leetcode.com/problems/subtree-of-another-tree/)
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The False Positive." A tree containing nodes with value `2` might look like a subtree, but the structure must match exactly.

**The Hero:** "The Recursive Matcher." For every node in the main tree `root`, check if the subtree rooted there is identical to `subRoot`.

**The Plot:**

1. Use `isSameTree` helper (from previous problem).
2. Base Case: If `root` is `None`, return `False` (empty tree contains nothing).
3. If `isSameTree(root, subRoot)` is true, return `True`.
4. Otherwise, recurse: `isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)`.

**The Twist (Failure):** **Complexity.** This is $O(N \cdot M)$. For a faster $O(N+M)$ solution, you'd need Merkle Hashing or String Serialization.

**Interview Signal:** Combining multiple **Recursive Functions**.

## 🚀 Approach & Intuition
Traverse root, calling isSameTree at each node.

### C++ Pseudo-Code
```cpp
class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root) return false;
        if (isSameTree(root, subRoot)) return true;
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
    
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q || p->val != q->val) return false;
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot M)$
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

- [LCA of BST](../lowest_common_ancestor_bst/PROBLEM.md) — Next in category
- [Same Tree](../same_tree/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
