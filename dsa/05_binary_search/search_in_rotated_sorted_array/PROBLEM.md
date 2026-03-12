#  🔍 Searching: Search in Rotated Sorted Array

## 📝 Description
[LeetCode 33](https://leetcode.com/problems/search-in-rotated-sorted-array/)
There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Target value is within the range of the data type.

## 🧠 The Engineering Story

**The Villain:** "The Pivot Pivot." A sorted array that has been rotated. You can't just binary search because the order is broken at the "inflection point."

**The Hero:** "The Half-Sorted Seeker." At any `mid` point, at least one half of the array MUST be sorted. Use this sorted half to decide where to go.

**The Plot:**

1. Pick a `mid`.
2. If `nums[left] <= nums[mid]`: The left half is sorted.
   - If `target` is within the left range, go left.
   - Else, go right.
3. Else: The right half must be sorted.
   - If `target` is within the right range, go right.
   - Else, go left.

**The Twist (Failure):** **The Duplicate Crisis.** This logic breaks if the array contains duplicates (e.g., `(To be detailed...)`), requiring a linear fallback.

**Interview Signal:** Mastery of **Advanced Binary Search** and conditional logic.

## 🚀 Approach & Intuition
(To be detailed...)

### Key Observations:

- Binary search can be applied not just to sorted arrays, but to any monotonic search space (Search on Answer).
- Be careful with the boundaries ($left, right$) and the condition for moving them to avoid infinite loops.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log N)$
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

- [Time Based KV Store](../time_based_key_value_store/PROBLEM.md) — Next in category
- [Find Min in Rotated Array](../find_minimum_in_rotated_sorted_array/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
