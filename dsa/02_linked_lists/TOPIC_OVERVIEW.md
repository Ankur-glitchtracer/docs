# 🔗 Topic Overview: Linked Lists

Linked Lists test your mastery of pointers and memory management. Unlike arrays, they are not contiguous, making them ideal for constant-time insertions and deletions at known positions.

## 🔑 Key Concepts Checklist
- [ ] **Dummy Head:** Simplifying edge cases like deleting the actual head or merging lists.
- [ ] **Fast & Slow Pointers:** The "Tortoise and Hare" algorithm for cycle detection and finding the middle.
- [ ] **Pointer Reversal:** Changing the direction of links in-place.
- [ ] **Multiple Pointers:** Tracking previous, current, and next nodes simultaneously.

## 🎯 Essential Problem Checklist (95% Coverage)
| Problem | Key Concept | Difficulty |
| :--- | :--- | :--- |
| **Reverse Linked List** | Iterative/Recursive Reversal | Easy |
| **Linked List Cycle** | Fast & Slow Pointers | Easy |
| **Merge Two Sorted Lists** | Dummy Head / Recursion | Easy |
| **Remove Nth Node From End** | Two Pointers (Fixed gap) | Medium |
| **Reorder List** | Middle + Reverse + Merge | Medium |
| **Intersection of Two Lists** | Two Pointers / Length difference | Easy |
| **Add Two Numbers** | Math + Iteration | Medium |
| **Linked List Cycle II** | Floyd's Cycle Finding | Medium |
| **LRU Cache** | Doubly Linked List + Map | Medium |
| **Merge K Sorted Lists** | Min Heap / Divide & Conquer | Hard |
| **Reverse Nodes in k-Group** | Sub-list Reversal | Hard |

## ⏱️ Complexity Cheatsheet
| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| Access | $O(N)$ | $O(1)$ |
| Search | $O(N)$ | $O(1)$ |
| Insertion at Head | $O(1)$ | $O(1)$ |
| Deletion at Head | $O(1)$ | $O(1)$ |
| Deletion (known node) | $O(1)$* (requires pointer to prev) | $O(1)$ |

## 📚 Recommended Reading (CP-Algorithms)
- [Stack and Queue Modification](https://cp-algorithms.com/data_structures/stack_queue_modification.html) (Implementation concepts)
- [Fundamentals: Time/Space Complexity](https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674a803d0c1/)

## 🔗 External References
- [Floyd's Cycle-Finding Algorithm (Visualization)](https://visualgo.net/en/list)
- [Linked List Data Structure (GeeksForGeeks)](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [Dummy Nodes in Linked Lists](https://www.linkedin.com/pulse/dummy-nodes-linked-lists-amit-kumar-/)
