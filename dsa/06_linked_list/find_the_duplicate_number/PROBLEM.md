#  🕵️ Linked Lists: Find the Duplicate Number

## 📝 Description
[LeetCode 287](https://leetcode.com/problems/find-the-duplicate-number/)
Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive. There is only one repeated number in `nums`, return this repeated number. You must solve the problem without modifying the array `nums` and uses only constant extra space.

## 🛠️ Requirements/Constraints

- Number of nodes is between 0 and 5000.
- $-1000 \le Node.val \le 1000$

## 🧠 The Engineering Story

**The Villain:** "The Constraints." Find a duplicate in an array of $N+1$ integers (range 1 to $N$) in $O(N)$ time, $O(1)$ space, without modifying the array. Sorting is banned ($O(N \log N)$ or modifies). Sets are banned ($O(N)$ space).

**The Hero:** "The Cycle Detective." Treat the array values as pointers (`val` points to index `val`). Since there's a duplicate, two indices point to the same value, creating a cycle.

**The Plot:**

1. This is exactly **Linked List Cycle II**.
2. **Phase 1:** Fast/Slow pointers to find intersection.
3. **Phase 2:** Reset `slow` to start. Move both `slow` and `fast` one step at a time.
4. They will meet at the entrance of the cycle (the duplicate number).

**The Twist (Failure):** **The Zero-Indexing.** If values were `0` to `N-1`, index `0` could point to itself `0`, forming a self-loop. The problem guarantees `1` to `N` so index 0 is always a safe entry point.

**Interview Signal:** Reducing array problems to **Graph/Cycle Detection**.

## 🚀 Approach & Intuition
Treat indices as nodes and values as pointers.

### C++ Pseudo-Code
```cpp
int findDuplicate(vector<int>& nums) {
    int slow = 0, fast = 0;
    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (slow != fast);
    
    slow = 0;
    while (slow != fast) {
        slow = nums[slow];
        fast = nums[fast];
    }
    return slow;
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

- [LRU Cache](../lru_cache/PROBLEM.md) — Next in category
- [Linked List Cycle](../linked_list_cycle/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
