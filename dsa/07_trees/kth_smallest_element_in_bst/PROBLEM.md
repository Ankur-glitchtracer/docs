#  🌲 Tree: Kth Smallest Element in a BST

## 📝 Description
[LeetCode 230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)
Given the `root` of a binary search tree, and an integer `k`, return the `k`th smallest value (1-indexed) of all the values of the nodes in the tree.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and $10^4$.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Full Sort." Dumping all values into an array and sorting them ($O(N \log N)$). Ignores the BST property.

**The Hero:** "The In-Order Traversal." In-order traversal (Left -> Root -> Right) of a BST yields sorted values inherently.

**The Plot:**

1. Perform iterative In-Order traversal (Stack).
2. Keep a counter `k`.
3. Decrement `k` each time we process a node (after returning from left child).
4. When `k == 0`, we found the answer.

**The Twist (Failure):** **Modifying the Tree.** If we could modify the tree, we could augment nodes with `subtree_size` counts to make this $O(H)$ lookup. Without modification, $O(N)$ traversal is best.

**Interview Signal:** Mastery of **Tree Traversal Properties**.

## 🚀 Approach & Intuition
Traverse in sorted order until kth element.

### C++ Pseudo-Code
```cpp
int kthSmallest(TreeNode* root, int k) {
    stack<TreeNode*> s;
    TreeNode* curr = root;
    while (curr || !s.empty()) {
        while (curr) {
            s.push(curr);
            curr = curr->left;
        }
        curr = s.top(); s.pop();
        k--;
        if (k == 0) return curr->val;
        curr = curr->right;
    }
    return -1;
}
```

### Key Observations:

- Most tree problems can be solved using either DFS (recursion) or BFS (queue).
- In-order traversal of a Binary Search Tree (BST) yields elements in sorted order.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(H + k)$
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

- [Build Tree Pre/Inorder](../construct_binary_tree_from_preorder_and_inorder/PROBLEM.md) — Next in category
- [Validate BST](../validate_binary_search_tree/PROBLEM.md) — Previous in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
