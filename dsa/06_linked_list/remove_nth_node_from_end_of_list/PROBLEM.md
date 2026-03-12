#  ➖ Linked Lists: Remove Nth Node From End of List

## 📝 Description
[LeetCode 19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
Given the `head` of a linked list, remove the `n`th node from the end of the list and return its head.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Unknown Length." You need to remove the $N^{th}$ node from the end, but you don't know how long the list is. The naive way is two passes: one to count length, one to remove.

**The Hero:** "The Fixed-Gap Sliding Window." Maintain two pointers with a gap of `n` nodes between them.

**The Plot:**

1. Move `fast` pointer `n` steps ahead.
2. If `fast` is `None` (already at end), it means we need to remove the head. Return `head.next`.
3. Move `slow` and `fast` together until `fast` hits the last node.
4. `slow` is now just before the target node. `slow.next = slow.next.next`.

**The Twist (Failure):** **The Off-by-One.** You want `slow` to be at `target - 1`, not `target`. That's why we stop when `fast` is at the *last* node, not `None`.

**Interview Signal:** Single-pass optimization logic.

## 🚀 Approach & Intuition
Advance fast pointer by n, then move both.

### C++ Pseudo-Code
```cpp
ListNode* removeNthFromEnd(ListNode* head, int n) {
    ListNode *dummy = new ListNode(0, head);
    ListNode *left = dummy, *right = head;
    
    while (n > 0 && right) {
        right = right->next;
        n--;
    }
    
    while (right) {
        left = left->next;
        right = right->next;
    }
    
    left->next = left->next->next;
    return dummy->next;
}
```

### Key Observations:

- Always consider using a dummy head node to simplify edge cases like inserting at the head or deleting the only node.
- Fast and slow pointers are a common pattern for finding the middle or detecting cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ (One pass)
    - **Space Complexity:** $O(1)$

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

- [Copy List Random Pointer](../copy_list_with_random_pointer/PROBLEM.md) — Next in category
- [Reorder List](../reorder_list/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
