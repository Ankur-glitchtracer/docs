#  🌲 Trees: Invert Binary Tree

## 📝 Description
[LeetCode 226](https://leetcode.com/problems/invert-binary-tree/)
Given the `root` of a binary tree, invert the tree, and return its root.

## 🛠️ Requirements/Constraints

- The number of nodes in the tree is in the range $[0, 100]$.
- $-100 \le Node.val \le 100$

## 🧠 The Engineering Story

**The Villain:** "The Mirror Image Challenge." Changing the perspective of an entire hierarchy without losing the connection between nodes.

**The Hero:** "The Level-by-Level Swapper." Visit every node and swap its left and right children.

**The Plot:**

1. If node is `None`, return.
2. Swap `node.left` and `node.right`.
3. Recursively call for `node.left` and `node.right`.

**The Twist (Failure):** **The Lost Reference.** Swapping children before you've finished traversing one side, making it impossible to find the original children if you aren't careful with the recursion.

**Interview Signal:** Mastery of **Basic Tree Manipulation**. (Famously requested by Google even for the creator of Homebrew).

## 🚀 Approach & Intuition
To invert a tree, we need to visit every node and swap its left and right children. This is a classic recursive problem: if we can invert the left subtree and the right subtree, and then swap them, the whole tree becomes inverted.

### Key Observations:

- The base case is a `null` node.
- A post-order or pre-order traversal both work, as long as you swap the children.
- The structure of the tree remains the same, only the pointers are mirrored.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ where $N$ is the number of nodes in the tree. We must visit every node once.
    - **Space Complexity:** $O(H)$ where $H$ is the height of the tree, representing the recursive stack depth. In the worst case (skewed tree), $O(N)$.

## 💻 Solution Implementation

```python
--8<-- "dsa/07_trees/invert_binary_tree/solution.py"
```

!!! success "Aha! Moment"
    Inversion is just a swap at every level. It's like looking at the tree in a mirror—what was on the left must now be on the right, all the way down to the leaves.

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you check if two trees are mirrors of each other (Symmetric Tree)?
- **Scale Question:** If the tree is too large for a single machine's memory, how would you process the inversion in a distributed graph database?
- **Edge Case Probe:** Does your solution work for an extremely unbalanced tree (essentially a linked list) without hitting a stack overflow?

## 🔗 Related Problems

- [Max Depth of Binary Tree](../maximum_depth_of_binary_tree/PROBLEM.md) — Next in category
- [Implement Trie](../../08_tries/implement_trie/PROBLEM.md) — Prerequisite for Tries
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite for Heap / Priority Queue
- [Subsets](../../10_backtracking/subsets/PROBLEM.md) — Prerequisite for Backtracking
