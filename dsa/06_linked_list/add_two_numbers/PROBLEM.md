#  ➕ Linked Lists: Add Two Numbers

## 📝 Description
[LeetCode 2](https://leetcode.com/problems/add-two-numbers/)
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Overflow." Adding two numbers can result in a sum larger than what a 64-bit integer can hold. Linked lists allow infinite precision.

**The Hero:** "The Grade-School Math." Adding digit by digit, carrying over the remainder.

**The Plot:**

1. Initialize `carry = 0`.
2. Iterate while `l1` or `l2` or `carry` is non-zero.
3. `sum = (l1.val if l1) + (l2.val if l2) + carry`.
4. `digit = sum % 10`, `carry = sum / 10`.
5. Create new node with `digit`.

**The Twist (Failure):** **The Final Carry.** Forgetting to check if `carry > 0` after the loops end (e.g., `5 + 5 = 10`, extra node `1` needed).

**Interview Signal:** Handling **State Persistence (Carry)** across iterations.

## 🚀 Approach & Intuition
Sum nodes + carry.

### C++ Pseudo-Code
```cpp
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(0);
    ListNode* curr = dummy;
    int carry = 0;
    
    while (l1 || l2 || carry) {
        int v1 = l1 ? l1->val : 0;
        int v2 = l2 ? l2->val : 0;
        
        int val = v1 + v2 + carry;
        carry = val / 10;
        val = val % 10;
        
        curr->next = new ListNode(val);
        curr = curr->next;
        
        if (l1) l1 = l1->next;
        if (l2) l2 = l2->next;
    }
    return dummy->next;
}
```

### Key Observations:

- Always consider using a dummy head node to simplify edge cases like inserting at the head or deleting the only node.
- Fast and slow pointers are a common pattern for finding the middle or detecting cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\max(N, M))$
    - **Space Complexity:** $O(\max(N, M))$ (Result list)

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

- [Linked List Cycle](../linked_list_cycle/PROBLEM.md) — Next in category
- [Copy List Random Pointer](../copy_list_with_random_pointer/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
