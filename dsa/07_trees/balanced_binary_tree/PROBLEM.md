#  🌲 Tree: Balanced Binary Tree

## 📝 Description
[LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/)
Given a binary tree, determine if it is height-balanced. For this problem, a height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Skewed Tree." A tree that looks like a linked list ($O(N)$ lookup). We want to detect this.

**The Hero:** "The Early Exit." Check height balance from bottom-up. If any subtree is unbalanced, the whole tree is unbalanced.

**The Plot:**

1. Use a helper function `check(node)` that returns the height.
2. If `node` is `None`, return 0.
3. `left = check(node.left)`, `right = check(node.right)`.
4. If `left == -1` or `right == -1` or `abs(left - right) > 1`: Return -1 (Indicator for unbalanced).
5. Otherwise return `1 + max(left, right)`.

**The Twist (Failure):** **Top-Down Checking.** Calling `height()` on every node results in $O(N^2)$. Bottom-up is $O(N)$.

**Interview Signal:** Optimizing **Tree Validation**.

## 🚀 Approach & Intuition
Return -1 if unbalanced, otherwise return height.

### C++ Pseudo-Code
```cpp
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return check(root) != -1;
    }
    
    int check(TreeNode* node) {
        if (!node) return 0;
        int l = check(node->left);
        if (l == -1) return -1;
        int r = check(node->right);
        if (r == -1) return -1;
        
        if (abs(l - r) > 1) return -1;
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

- [Same Tree](../same_tree/PROBLEM.md) — Next in category
- [Diameter of Binary Tree](../diameter_of_binary_tree/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
