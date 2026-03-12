#  🌲 Tree: Validate Binary Search Tree

## 📝 Description
[LeetCode 98](https://leetcode.com/problems/validate-binary-search-tree/)
Given the `root` of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Local Check." Checking only `left < node < right`. This fails for trees like `5 -> 4 -> 10`. 10 is > 4 (valid locally), but 10 is > 5 (invalid globally, should be left of 5).

**The Hero:** "The Range Enforcer." Every node must satisfy a range `(min, max)`.

**The Plot:**

1. Start with `(-inf, +inf)`.
2. When moving left, the new max is `node.val`. Range becomes `(min, node.val)`.
3. When moving right, the new min is `node.val`. Range becomes `(node.val, max)`.
4. If `node.val` violates the current range, return `False`.

**The Twist (Failure):** **Integer Limits.** Use `long long` or nullable types to handle `INT_MAX` inputs correctly.

**Interview Signal:** Understanding **Global Invariants** in recursion.

## 🚀 Approach & Intuition
Pass valid range (min, max) down the recursion.

### C++ Pseudo-Code
```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return validate(root, LONG_MIN, LONG_MAX);
    }
    
    bool validate(TreeNode* node, long minVal, long maxVal) {
        if (!node) return true;
        if (node->val <= minVal || node->val >= maxVal) return false;
        return validate(node->left, minVal, node->val) &&
               validate(node->right, node->val, maxVal);
    }
};
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

- [Kth Smallest in BST](../kth_smallest_element_in_bst/PROBLEM.md) — Next in category
- [Count Good Nodes](../count_good_nodes_in_binary_tree/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
