#  🔍 Searching: Binary Search

## 📝 Description
[LeetCode 704](https://leetcode.com/problems/binary-search/)
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`.

## 🛠️ Requirements/Constraints

- $1 <= nums.length <= 10^4$
- $-10^4 < nums[i], target < 10^4$
- All integers in `nums` are unique.
- `nums` is sorted in ascending order.

## 🧠 The Engineering Story

**The Villain:** "The Linear Crawler." Checking every single element in a list of 1 billion items ($O(N)$). If the item is at the end, your user waits for minutes.

**The Hero:** "The Great Divider." Halving the search space at every step ($O(\log N)$). 1 billion items are narrowed down to the target in just 30 steps.

**The Plot:**

1. `low = 0`, `high = n-1`.
2. While `low <= high`:
   - `mid = low + (high - low) // 2` (Avoiding overflow).
   - If `target == nums[mid]`, return `mid`.
   - If `target < nums[mid]`, search the left half (`high = mid - 1`).
   - If `target > nums[mid]`, search the right half (`low = mid + 1`).

**The Twist (Failure):** **The Infinite Loop.** Forgetting to update `low` or `high` with `mid ± 1`, or using an incorrect `while` condition (`low < high` vs `low <= high`).

**Interview Signal:** Mastery of **Logarithmic Efficiency** and basic algorithm precision.

## 🚀 Approach & Intuition
Binary search leverages the sorted property of the input. By comparing the target with the middle element, we can discard half of the remaining elements in a single step.

### Key Observations:

- The array must be sorted.
- `low <= high` ensures we check the last remaining element.
- `mid = low + (high - low) // 2` is safer than `(low + high) // 2` to prevent integer overflow in some languages.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log N)$ - The search space is halved in each iteration.
    - **Space Complexity:** $O(1)$ - Only a few pointers are used.

## 💻 Solution Implementation

```python
--8<-- "dsa/05_binary_search/binary_search/solution.py"
```

!!! success "Aha! Moment"
    The "sorted" property is the key. Without it, we are forced to use linear search. With it, we gain exponential speedup.

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you find the first and last position of an element in a sorted array with duplicates?
- **Scale Question:** If the 'array' is actually a massive sorted file on S3, how do you perform binary search using HTTP Range requests?
- **Edge Case Probe:** How do you prevent integer overflow when calculating the 'mid' index in languages like C++ or Java?

## 🔗 Related Problems

- [Search 2D Matrix](../search_2d_matrix/PROBLEM.md) — Next in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
- [Bubble Sort](../../19_sorting/bubble_sort/PROBLEM.md) — Prerequisite: Sorting
