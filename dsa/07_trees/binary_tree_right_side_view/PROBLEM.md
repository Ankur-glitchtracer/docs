#  🌲 Tree: Binary Tree Right Side View

## 📝 Description
[LeetCode 199](https://leetcode.com/problems/binary-tree-right-side-view/)
Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Blocked View." You can't just take all right children (`curr.right`). A left child might be visible if the right branch ends early.

**The Hero:** "The Level Order Snapshot." Perform BFS (Level Order). The last element added to the queue at each level is the rightmost node.

**The Plot:**

1. Initialize queue with root.
2. While queue is not empty:
   - Determine `level_size`.
   - Iterate `i` from 0 to `level_size`.
   - Pop node. Add children.
   - If `i == level_size - 1`, this is the rightmost node. Add to result.

**The Twist (Failure):** **The DFS Alternative.** You can also use DFS (Root -> Right -> Left). If `result.size() == depth`, add the node. This captures the first node visited at each depth (which is the rightmost).

**Interview Signal:** Mastery of **BFS Variations**.

## 🚀 Approach & Intuition
Capture the last element of each level.

### C++ Pseudo-Code
```cpp
vector<int> rightSideView(TreeNode* root) {
    if (!root) return {};
    vector<int> res;
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int n = q.size();
        for (int i = 0; i < n; i++) {
            TreeNode* node = q.front(); q.pop();
            if (i == n - 1) res.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
    }
    return res;
}
```

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(D)$ (Diameter/Width of tree)

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

- [Count Good Nodes](../count_good_nodes_in_binary_tree/PROBLEM.md) — Next in category
- [Level Order Traversal](../binary_tree_level_order_traversal/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
