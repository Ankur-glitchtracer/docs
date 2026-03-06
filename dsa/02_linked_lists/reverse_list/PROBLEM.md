# 🔄 Linked Lists: Reverse Linked List

## 📝 Description
[LeetCode 206](https://leetcode.com/problems/reverse-linked-list/)
Given the `head` of a singly linked list, reverse the list and return its new head.

## 🚀 Approach 1: Iterative (Pointers) - **Optimal**
Traverse the list and flip the `next` pointer of each node to point to its predecessor.

### C++ Pseudo-Code
```cpp
ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* nextNode = curr->next; // Save next
        curr->next = prev;               // Flip link
        prev = curr;                     // Move prev
        curr = nextNode;                 // Move curr
    }
    return prev;
}
```

!!! success "Analysis"
    - **Time:** $O(N)$ - One pass through the list.
    - **Space:** $O(1)$ - Constant extra space.

---

## 🚀 Approach 2: Recursive
Divide the problem into reversing the "rest of the list" and then pointing the current node to its predecessor.

### C++ Pseudo-Code
```cpp
ListNode* reverseList(ListNode* head) {
    if (!head || !head->next) return head;
    
    ListNode* newHead = reverseList(head->next);
    head->next->next = head; // Point next node back to current
    head->next = nullptr;    // Set current next to null
    
    return newHead;
}
```

!!! info "Analysis"
    - **Time:** $O(N)$ - Visits each node.
    - **Space:** $O(N)$ - Stack depth for the recursion.
