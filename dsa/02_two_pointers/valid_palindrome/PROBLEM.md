#  ↔️ Two Pointers: Valid Palindrome

## 📝 Description
[LeetCode 125](https://leetcode.com/problems/valid-palindrome/)
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## 🛠️ Requirements/Constraints

- $1 <= s.length <= 2 * 10^5$
- `s` consists only of printable ASCII characters.

## 🧠 The Engineering Story

**The Villain:** "The Memory Allocator." Creating a new string just to filter out non-alphanumeric characters or reverse it ($O(N)$ space).

**The Hero:** "The In-Place Converger." Comparing characters from both ends inwards, skipping garbage characters on the fly.

**The Plot:**

1. Initialize `left = 0`, `right = s.length - 1`.
2. While `left < right`:
   - If `s[left]` is not alphanumeric, increment `left`.
   - If `s[right]` is not alphanumeric, decrement `right`.
   - If `lower(s[left]) != lower(s[right])`, return `false`.
   - Move both pointers inward.

**The Twist (Failure):** **The Empty String.** Handling strings with no valid characters (e.g., ".,"). The logic must ensure pointers don't cross bounds wildly.

**Interview Signal:** Mastery of **In-Place String Manipulation**.

## 🚀 Approach & Intuition
The core idea is to use two pointers starting at opposite ends of the string and moving toward the center. We only compare alphanumeric characters, effectively ignoring whitespace and punctuation without needing to pre-process the string into a new object.

### Key Observations:

- We can skip non-alphanumeric characters using nested `while` loops.
- `tolower()` ensures the comparison is case-insensitive.
- The `left < right` condition handles both even and odd length palindromes.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ - We traverse the string at most once.
    - **Space Complexity:** $O(1)$ - No extra space allocated.

## 💻 Solution Implementation

```python
--8<-- "dsa/02_two_pointers/valid_palindrome/solution.py"
```

!!! success "Aha! Moment"
    The trick is skipping "garbage" characters on the fly. By moving the pointers until they hit valid characters, we achieve $O(1)$ space, whereas a naive "filter and reverse" approach would use $O(N)$ space.

## 🎤 Interview Follow-ups

- **Harder Variant:** What if you are allowed to delete at most one character to make it a palindrome (Valid Palindrome II)?
- **Scale Question:** How would you check if a massive file (e.g., 10GB) is a palindrome without loading it all into RAM?
- **Edge Case Probe:** Does your solution correctly ignore non-alphanumeric characters and handle case sensitivity?

## 🔗 Related Problems

- [Two Sum II](../two_sum_ii/PROBLEM.md) — Next in category
- [Best Time to Buy/Sell Stock](../../03_sliding_window/best_time_to_buy_sell_stock/PROBLEM.md) — Prerequisite for Sliding Window
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
- [Reverse Linked List](../../06_linked_list/reverse_list/PROBLEM.md) — Prerequisite for Linked List
