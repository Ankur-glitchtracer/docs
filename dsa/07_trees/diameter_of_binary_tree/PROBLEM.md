#  🌲 Tree: Diameter of Binary Tree

## 📝 Description
[LeetCode 543](https://leetcode.com/problems/diameter-of-binary-tree/)
Given the `root` of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Longest Path Paradox." The longest path might not pass through the root. It could be entirely within the left or right subtree.

**The Hero:** "The Height Reporter." While calculating height, also calculate the diameter passing through the current node (`left_height + right_height`).

**The Plot:**

1. Initialize a global/class variable `max_diameter = 0`.
2. Define a recursive `height(node)` function.
   - Base case: If `node` is `None`, height is 0.
   - Recursive step: `L = height(node.left)`, `R = height(node.right)`.
   - **Update Diameter:** `max_diameter = max(max_diameter, L + R)`.
   - Return `1 + max(L, R)`.

**The Twist (Failure):** **Edges vs Nodes.** The problem asks for the length of the path in *edges*, which corresponds to `L + R`. If counting nodes, it would be `L + R + 1`.

**Interview Signal:** Calculating **Properties during Traversal**.

## 🚀 Approach & Intuition
Compute diameter while computing height.

### C++ Pseudo-Code
```cpp
class Solution {
    int maxD = 0;
public:
    int diameterOfBinaryTree(TreeNode* root) {
        height(root);
        return maxD;
    }
    
    int height(TreeNode* node) {
        if (!node) return 0;
        int l = height(node->left);
        int r = height(node->right);
        maxD = max(maxD, l + r);
        return 1 + max(l, r);
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

- [Balanced Binary Tree](../balanced_binary_tree/PROBLEM.md) — Next in category
- [Max Depth of Binary Tree](../maximum_depth_of_binary_tree/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
