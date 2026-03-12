#  🌲 Tree: Serialize and Deserialize Binary Tree

## 📝 Description
[LeetCode 297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment. Design an algorithm to serialize and deserialize a binary tree.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Structure Loss." If you just print nodes [1, 2, 3], you don't know if 3 is a left or right child.

**The Hero:** "The Null Sentinel." Explicitly recording 'None' or 'Null' values preserves the structure.

**The Plot:**

1. **Serialize (Preorder):** DFS. If node, append `val,`. If null, append `N,`.
2. **Deserialize:** Split string by comma. Use a Queue (or iterator).
   - Pop token.
   - If 'N', return null.
   - Else, create node. `node.left = recurse()`, `node.right = recurse()`.

**The Twist (Failure):** **Queue vs Recursion.** Preorder is easiest with recursion/iterator. Level order requires a queue. Both work, but Preorder is often cleaner to code.

**Interview Signal:** Knowledge of **Data Marshaling**.

## 🚀 Approach & Intuition
Use "N" to represent null nodes.

### C++ Pseudo-Code
```cpp
class Codec {
public:
    string serialize(TreeNode* root) {
        if (!root) return "N,";
        return to_string(root->val) + "," + serialize(root->left) + serialize(root->right);
    }

    TreeNode* deserialize(string data) {
        stringstream ss(data);
        string item;
        queue<string> q;
        while (getline(ss, item, ',')) q.push(item);
        return decode(q);
    }
    
    TreeNode* decode(queue<string>& q) {
        string s = q.front(); q.pop();
        if (s == "N") return nullptr;
        TreeNode* root = new TreeNode(stoi(s));
        root->left = decode(q);
        root->right = decode(q);
        return root;
    }
};
```

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(N)$

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

- [Max Path Sum](../binary_tree_maximum_path_sum/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
- [Subsets](../../10_backtracking/subsets/PROBLEM.md) — Prerequisite for Backtracking
