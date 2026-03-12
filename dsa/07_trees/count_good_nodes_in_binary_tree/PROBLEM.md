#  🌲 Tree: Count Good Nodes in Binary Tree

## 📝 Description
[LeetCode 1448](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)
Given a binary tree `root`, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Memoryless Walk." Traversing the tree but forgetting the maximum value seen so far in the current path.

**The Hero:** "The Path Context." Pass the `max_val` down during recursion.

**The Plot:**

1. DFS function `dfs(node, max_val)`.
2. If `node.val >= max_val`: It's a good node! Increment count. Update `max_val`.
3. Recurse left and right with the new (or existing) `max_val`.

**The Twist (Failure):** **Global vs Local Max.** The "max" is only relevant for the *current path*. When backtracking, the max should revert. Passing by value handles this automatically.

**Interview Signal:** Passing **State in Recursion**.

## 🚀 Approach & Intuition
Pass maximum value seen so far down the recursion.

### C++ Pseudo-Code
```cpp
class Solution {
public:
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
    
    int dfs(TreeNode* node, int maxVal) {
        if (!node) return 0;
        int res = (node->val >= maxVal) ? 1 : 0;
        maxVal = max(maxVal, node->val);
        res += dfs(node->left, maxVal);
        res += dfs(node->right, maxVal);
        return res;
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

- [Validate BST](../validate_binary_search_tree/PROBLEM.md) — Next in category
- [Right Side View](../binary_tree_right_side_view/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
