#  👯 Linked Lists: Copy List with Random Pointer

## 📝 Description
[LeetCode 138](https://leetcode.com/problems/copy-list-with-random-pointer/)
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`. Construct a deep copy of the list.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Deep Copy Dilemma." If you just copy `next` pointers, you get a new list. But how do you connect `random` pointers if the target nodes haven't been created yet?

**The Hero:** "The Interwoven Weave (or Hash Map)."

**The Plot:**

1. (To be detailed...)
2. (To be detailed...)

**The Twist (Failure):** **The Interwoven Strategy ($O(1)$ Space).**

**Interview Signal:** Handling **Complex Object Deep Copies**.

## 🚀 Approach & Intuition
Map original nodes to new nodes.

### C++ Pseudo-Code
```cpp
Node* copyRandomList(Node* head) {
    if (!head) return nullptr;
    unordered_map<Node*, Node*> map;
    
    Node* curr = head;
    while (curr) {
        map[curr] = new Node(curr->val);
        curr = curr->next;
    }
    
    curr = head;
    while (curr) {
        map[curr]->next = map[curr->next];
        map[curr]->random = map(To be detailed...);
        curr = curr->next;
    }
    return map[head];
}
```

### Key Observations:

- Always consider using a dummy head node to simplify edge cases like inserting at the head or deleting the only node.
- Fast and slow pointers are a common pattern for finding the middle or detecting cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(N)$ (Map) or $O(1)$ (Interweaving)

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

- [Add Two Numbers](../add_two_numbers/PROBLEM.md) — Next in category
- [Remove Nth Node From End](../remove_nth_node_from_end_of_list/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
