#  💾 Linked Lists: LRU Cache

## 📝 Description
[LeetCode 146](https://leetcode.com/problems/lru-cache/)
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The $O(N)$ Eviction." Keeping a list of used items is easy. Moving an item to the front or finding the least recently used item usually takes $O(N)$. We need $O(1)$.

**The Hero:** "The HashMap + Doubly Linked List."

**The Plot:**

1. **HashMap:** Maps `key` -> `Node*` (for $O(1)$ access).
2. **Doubly Linked List:** Maintains order.
   - **Head:** Most Recently Used (MRU).
   - **Tail:** Least Recently Used (LRU).
3. **Get:** Look up in map. If found, detach node and move to Head.
4. **Put:**
   - If key exists: Update value, move to Head.
   - If new: Create node, add to Head, add to Map.
   - If over capacity: Remove Tail node, remove from Map.

**The Twist (Failure):** **The Pointer Surgery.** Forgetting to update `prev.next` and `next.prev` when detaching a node. Using dummy head and tail simplifies this immensely.

**Interview Signal:** Designing **Composite Data Structures**.

## 🚀 Approach & Intuition
Map for access, DLL for ordering.

### C++ Pseudo-Code
```cpp
class LRUCache {
    // Node struct with prev, next, key, val
    // Map<int, Node*>
    // Dummy Head, Dummy Tail
    
    // Helper: removeNode(node)
    // Helper: insertAfterHead(node)
public:
    int get(int key) {
        if (!map.count(key)) return -1;
        Node* node = map[key];
        removeNode(node);
        insertAfterHead(node);
        return node->val;
    }
    
    void put(int key, int value) {
        if (map.count(key)) {
            removeNode(map[key]);
        }
        if (map.size() == capacity) {
            removeMap(tail->prev->key);
            removeNode(tail->prev);
        }
        insertAfterHead(new Node(key, value));
    }
};
```

### Key Observations:

- Always consider using a dummy head node to simplify edge cases like inserting at the head or deleting the only node.
- Fast and slow pointers are a common pattern for finding the middle or detecting cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(1)$ for both `get` and `put`.
    - **Space Complexity:** $O(C)$ where C is capacity.

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the input is sorted or has a limited range? Can you optimize space from $O(N)$ to $O(1)$?
- **Scale Question:** If the dataset is too large to fit in RAM, how would you use external sorting or a distributed hash table?
- **Edge Case Probe:** How does your solution handle duplicates, empty inputs, or extremely large integers?

## 🔗 Related Problems

- [Merge K Sorted Lists](../merge_k_sorted_lists/PROBLEM.md) — Next in category
- [Find the Duplicate Number](../find_the_duplicate_number/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
