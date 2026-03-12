#  🌲 Tree: Binary Tree Maximum Path Sum

## 📝 Description
[LeetCode 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root. Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Split Path." A path can go from left child -> root -> right child. This path *cannot* be passed up to the parent (because that would branch).

**The Hero:** "The Global Max Update." We separate what we *return* (one branch) from what we *calculate* (potential split).

**The Plot:**

1. DFS returns: `max_gain = node.val + max(left_gain, right_gain)`. This is the max path extending downwards.
2. Inside DFS, we calculate `current_path = node.val + left_gain + right_gain`. This represents a "split" at the current node.
3. Update global `max_sum` with `current_path`.

**The Twist (Failure):** **The Negative Gain.** If a subtree returns a negative sum, ignore it (treat as 0). Adding a negative branch only hurts the total sum.

**Interview Signal:** Managing **Global vs Local Optimization** logic.

## 🚀 Approach & Intuition
Calculate split path sum, return single branch sum.

### C++ Pseudo-Code
```cpp
class Solution {
    int maxSum = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return maxSum;
    }
    
    int dfs(TreeNode* node) {
        if (!node) return 0;
        
        // Ignore negative paths (max with 0)
        int left = max(dfs(node->left), 0);
        int right = max(dfs(node->right), 0);
        
        // Path splitting at this node
        maxSum = max(maxSum, node->val + left + right);
        
        // Return max path extending upwards
        return node->val + max(left, right);
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

- [Serialize/Deserialize Tree](../serialize_and_deserialize_binary_tree/PROBLEM.md) — Next in category
- [Build Tree Pre/Inorder](../construct_binary_tree_from_preorder_and_inorder/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
