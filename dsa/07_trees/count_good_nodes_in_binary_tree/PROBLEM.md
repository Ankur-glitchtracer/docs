---
impact: "Medium"
nr: false
confidence: 2
---
# 🌲 Tree: Count Good Nodes in Binary Tree

## 📝 Description
[LeetCode 1448](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)
Given a binary tree `root`, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X. Return the number of good nodes in the binary tree.

!!! info "Real-World Application"
    This relates to **Monotonic Path Analysis** in time-series hierarchies or finding peaks/records in a decision tree path.

## 🛠️ Constraints & Edge Cases
- Number of nodes is between 0 and $10^5$.
- $-10^4 \le Node.val \le 10^4$
- **Edge Cases to Watch:**
    - Root is always good.
    - Path values equal to max are good (`>=`).

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    A node is "good" if it's $\ge$ the maximum value seen *so far* on the path from the root. We just need to carry this `max_val` context down during recursion.

### 🐢 Brute Force (Naive)
For each node, trace back to root to check validity.
- **Time Complexity:** $O(N^2)$ (skewed tree).

### 🐇 Optimal Approach (DFS)
1.  Define `dfs(node, maxVal)`.
2.  If `node.val >= maxVal`:
    - Increment count (1).
    - Update `maxVal = node.val`.
3.  Recurse Left and Right with new `maxVal`.
4.  Sum up results.

### 🧩 Visual Tracing
```mermaid
graph TD
    A[3 (Max:3)] --> B[1 (Max:3, Not Good)]
    A --> C[4 (Max:4, Good)]
    C --> D[1 (Max:4, Not Good)]
    C --> E[5 (Max:5, Good)]
    Res[Total: 3, 4, 5 = 3 nodes]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ — Visit every node once.
- **Space Complexity:** $\mathcal{O}(H)$ — Recursion depth.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Find paths where *all* nodes are increasing?

## 🔗 Related Problems
- [Validate Binary Search Tree](../validate_binary_search_tree/PROBLEM.md) — Next in category
