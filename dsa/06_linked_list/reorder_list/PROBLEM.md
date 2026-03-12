#  🔀 Linked Lists: Reorder List

## 📝 Description
[LeetCode 143](https://leetcode.com/problems/reorder-list/)
You are given the head of a singly linked-list. The list can be represented as:
`L0 → L1 → … → Ln - 1 → Ln`
Reorder the list to be on the following form:
`L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Random Access Need." You need to merge `L[0], L[n], L[1], L[n-1]`. Linked lists don't support $O(1)$ random access, so fetching `L[n-1]` repeatedly makes this $O(N^2)$.

**The Hero:** "The Split-Reverse-Merge Combo." Break the problem into three primitives we already know.

**The Plot:**

1. **Find Middle:** Use slow/fast pointers to split the list into two halves.
2. **Reverse Second Half:** Reverse the right half of the list ($O(N)$).
3. **Merge:** Alternate nodes from the left and the (now reversed) right list.

**The Twist (Failure):** **The Cycle Risk.** If you don't sever the connection between the two halves (`middle.next = None`), you'll create a cycle during the merge.

**Interview Signal:** Mastery of **Algorithm Composition**.

## 🚀 Approach & Intuition
Combine three standard LL algorithms.

### C++ Pseudo-Code
```cpp
void reorderList(ListNode* head) {
    if (!head) return;
    
    // 1. Find middle
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // 2. Reverse second half
    ListNode *prev = nullptr, *curr = slow->next, *tmp;
    slow->next = nullptr;
    while (curr) {
        tmp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = tmp;
    }
    
    // 3. Merge
    ListNode *first = head, *second = prev;
    while (second) {
        ListNode *tmp1 = first->next, *tmp2 = second->next;
        first->next = second;
        second->next = tmp1;
        first = tmp1;
        second = tmp2;
    }
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

- [Remove Nth Node From End](../remove_nth_node_from_end_of_list/PROBLEM.md) — Next in category
- [Merge Two Sorted Lists](../merge_sorted_lists/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
