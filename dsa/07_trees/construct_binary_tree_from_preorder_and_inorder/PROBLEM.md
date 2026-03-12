#  🌲 Tree: Construct Binary Tree from Preorder and Inorder Traversal

## 📝 Description
[LeetCode 105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Ambiguous List." A single traversal isn't enough to reconstruct a tree. You need two perspectives.

**The Hero:** "The Root Finder."

**The Plot:**

1. Take `preorder[0]`. This is the `root`.
2. Find `root` inside `inorder` array (index `mid`).
3. Elements `inorder[0...mid]` are the Left Subtree.
4. Elements `inorder[mid+1...]` are the Right Subtree.
5. Recursively build left and right children using the corresponding segments of `preorder`.

**The Twist (Failure):** **Linear Search.** Searching for `root` in `inorder` takes $O(N)$. Total $O(N^2)$. Use a Hash Map to index `inorder` for $O(1)$ lookup -> Total $O(N)$.

**Interview Signal:** Converting **Linear Data to Hierarchical Structures**.

## 🚀 Approach & Intuition
Use Preorder for root, Inorder for boundaries.

### C++ Pseudo-Code
```cpp
class Solution {
    unordered_map<int, int> inMap;
    int preIdx = 0;
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) inMap[inorder[i]] = i;
        return build(preorder, 0, inorder.size() - 1);
    }
    
    TreeNode* build(vector<int>& preorder, int inStart, int inEnd) {
        if (inStart > inEnd) return nullptr;
        
        int rootVal = preorder[preIdx++];
        TreeNode* root = new TreeNode(rootVal);
        int mid = inMap[rootVal];
        
        root->left = build(preorder, inStart, mid - 1);
        root->right = build(preorder, mid + 1, inEnd);
        return root;
    }
};
```

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(N)$ (Hash Map)

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

- [Max Path Sum](../binary_tree_maximum_path_sum/PROBLEM.md) — Next in category
- [Kth Smallest in BST](../kth_smallest_element_in_bst/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
