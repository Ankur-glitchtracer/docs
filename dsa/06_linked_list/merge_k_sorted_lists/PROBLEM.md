#  📶 Linked Lists: Merge K Sorted Lists

## 📝 Description
[LeetCode 23](https://leetcode.com/problems/merge-k-sorted-lists/)
You are given an array of `k` linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Slow Consolidation." Merging lists one by one (`((L1+L2)+L3)+...`) takes $O(K \cdot N)$.

**The Hero:** "The Min-Heap (or Divide & Conquer)."

**The Plot:**

1. (To be detailed...)
2. (To be detailed...)

**The Twist (Failure):** **The Heap Object.** C++ heaps need a custom comparator to sort `ListNode*` by `val`.

**Interview Signal:** Knowledge of **$N \log K$** patterns.

## 🚀 Approach & Intuition
Keep the smallest head of all lists in a heap.

### C++ Pseudo-Code
```cpp
ListNode* mergeKLists(vector<ListNode*>& lists) {
    auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
    priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
    
    for (auto l : lists) if (l) pq.push(l);
    
    ListNode dummy(0);
    ListNode* curr = &dummy;
    
    while (!pq.empty()) {
        ListNode* top = pq.top(); pq.pop();
        curr->next = top;
        curr = curr->next;
        if (top->next) pq.push(top->next);
    }
    return dummy.next;
}
```

### Key Observations:

- Always consider using a dummy head node to simplify edge cases like inserting at the head or deleting the only node.
- Fast and slow pointers are a common pattern for finding the middle or detecting cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log K)$
    - **Space Complexity:** $O(K)$ (Heap) or $O(1)$ (Divide & Conquer iteratively)

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

- [Reverse Nodes in K Group](../reverse_nodes_in_k_group/PROBLEM.md) — Next in category
- [LRU Cache](../lru_cache/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
