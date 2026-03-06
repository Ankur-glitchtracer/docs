# 🌳 Tree: Binary Tree Level Order Traversal

## 📝 Description
[LeetCode 102](https://leetcode.com/problems/binary-tree-level-order-traversal/)
Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## 🚀 Approach 1: Iterative BFS (Queue) - **Optimal**
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

!!! success "Analysis"
    - **Time:** $O(N)$ - Visit every node once.
    - **Space:** $O(N)$ - Max queue size is the width of the tree (last level can be $N/2$).

---

## 🚀 Approach 2: Recursive DFS
DFS usually goes deep first, but we can simulate level order by passing the `level` index to the recursion.

### C++ Pseudo-Code
```cpp
void dfs(TreeNode* node, int level, vector<vector<int>>& result) {
    if (!node) return;
    
    // Ensure the vector has a list for this level
    if (result.size() == level) {
        result.push_back({});
    }
    
    result[level].push_back(node->val);
    
    dfs(node->left, level + 1, result);
    dfs(node->right, level + 1, result);
}
```

!!! warning "Caveats"
    - DFS uses the call stack $O(H)$, which can be $O(N)$ for a skewed tree.
    - BFS is generally intuitive for "Level Order," while DFS is better for "Path" problems.
