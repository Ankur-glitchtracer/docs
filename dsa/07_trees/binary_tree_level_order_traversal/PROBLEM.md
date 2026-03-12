#  🌳 Tree: Binary Tree Level Order Traversal

## 📝 Description
[LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/)
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Fog of War." Not knowing the shortest path or the "width" of a tree at a specific depth because you're diving deep into one branch (DFS).

**The Hero:** "The FIFO Queue (BFS)." Processing nodes layer by layer, ensuring you see every node at distance `D` before seeing anyone at `D+1`.

**The Plot:**

1. Initialize a `Queue` with the root.
2. While the queue is not empty, take a snapshot of its `size` (current level count).
3. Process exactly `size` nodes, adding their children back into the queue.
4. Add the level's results to the final list.

**The Twist (Failure):** **The Queue Bloat.** In a perfectly balanced tree, the last level contains $N/2$ nodes, requiring $O(N)$ space.

**Interview Signal:** Mastery of **Breadth-First Search** and level-by-level processing.

## 🚀 Approach & Intuition
Using a queue is the standard way to perform Breadth-First Search. We process nodes level by level.

### C++ Pseudo-Code
```cpp
vector<vector<int>> levelOrder(TreeNode* root) {
    if (!root) return {};
    vector<vector<int>> result;
    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int levelSize = q.size(); // Snapshot current level size
        vector<int> currentLevel;
        
        for (int i = 0; i < levelSize; i++) {
            TreeNode* node = q.front();
            q.pop();
            currentLevel.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        result.push_back(currentLevel);
    }
    return result;
}
```

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ (To be detailed...)
    - **Space Complexity:** $O(1)$ (To be detailed...)

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

- [Right Side View](../binary_tree_right_side_view/PROBLEM.md) — Next in category
- [LCA of BST](../lowest_common_ancestor_bst/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
