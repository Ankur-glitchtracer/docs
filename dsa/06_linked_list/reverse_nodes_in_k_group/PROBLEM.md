#  🔄 Linked Lists: Reverse Nodes in k-Group

## 📝 Description
[LeetCode 25](https://leetcode.com/problems/reverse-nodes-in-k-group/)
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list. `k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Partial Reversal." You need to reverse sub-segments of a list, but only if the segment has length `k`. If it's shorter (at the end), leave it alone.

**The Hero:** "The Look-Ahead & Reverse."

**The Plot:**

1. Iterate through the list to check if `k` nodes exist ahead.
2. If yes:
   - Identify the `groupStart` and `groupEnd`.
   - Reverse the links within this group.
   - Connect the previous group's tail to the new group's head.
   - Move pointers to the next group.
3. If no: Stop.

**The Twist (Failure):** **The Connection Logic.** After reversing `A->B->C` to `C->B->A`, `A` is now the tail. You must connect `A` to the *next* group (or `D`).

**Interview Signal:** Mastery of **Complex Pointer Manipulation**.

## 🚀 Approach & Intuition
Check k-length, reverse, connect.

### C++ Pseudo-Code
```cpp
ListNode* reverseKGroup(ListNode* head, int k) {
    ListNode* dummy = new ListNode(0, head);
    ListNode* groupPrev = dummy;
    
    while (true) {
        ListNode* kth = groupPrev;
        // Check if k nodes exist
        for (int i = 0; i < k && kth; i++) kth = kth->next;
        if (!kth) break;
        
        ListNode* groupNext = kth->next;
        
        // Reverse group
        ListNode* prev = groupNext, *curr = groupPrev->next;
        while (curr != groupNext) {
            ListNode* tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        
        // Connect
        ListNode* tmp = groupPrev->next;
        groupPrev->next = kth;
        groupPrev = tmp;
    }
    return dummy->next;
}
```

### Key Observations:

- Always consider using a dummy head node to simplify edge cases like inserting at the head or deleting the only node.
- Fast and slow pointers are a common pattern for finding the middle or detecting cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
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

- [Merge K Sorted Lists](../merge_k_sorted_lists/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
