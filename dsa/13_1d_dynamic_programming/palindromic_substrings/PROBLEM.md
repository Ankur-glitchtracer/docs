#  🪞 DP: Palindromic Substrings

## 📝 Description
[LeetCode 647](https://leetcode.com/problems/palindromic-substrings/)
Given a string `s`, return the number of palindromic substrings in it. A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Count." Similar to Longest Palindromic Substring, but now we count *all* of them. "aaa" has "a", "a", "a", "aa", "aa", "aaa" (6 total).

**The Hero:** "The Accumulating Expander." Same expand strategy. Every time you successfully expand (`s[l] == s[r]`), that's a valid palindrome. Increment count.

**The Plot:**

1. Initialize `count = 0`.
2. Iterate `i` from 0 to `n`.
3. Expand Odd: `l=i, r=i`. While valid: `count++`, expand.
4. Expand Even: `l=i, r=i+1`. While valid: `count++`, expand.

**The Twist (Failure):** **Double Counting.** Actually, expanding *is* the correct way to avoid double counting because every palindrome has a unique center.

**Interview Signal:** Reusing **Center Expansion** pattern.

## 🚀 Approach & Intuition
Count valid expansions.

### C++ Pseudo-Code
```cpp
int countSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        // Odd
        int l = i, r = i;
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            count++;
            l--; r++;
        }
        // Even
        l = i; r = i + 1;
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            count++;
            l--; r++;
        }
    }
    return count;
}
```

### Key Observations:

- Break down the problem into smaller sub-problems and store their results to avoid redundant calculations.
- Determine the base cases and the recurrence relation; bottom-up (tabulation) is often more space-efficient.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2)$
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you optimize the space complexity from $O(N^2)$ to $O(N)$? Can you solve it using a top-down vs bottom-up approach?
- **Scale Question:** If the DP table is too large for memory, can you use 'Check-pointing' or a sliding window of rows to save space?
- **Edge Case Probe:** What are the base cases for empty or single-element inputs? How do you handle negative values if they aren't expected?

## 🔗 Related Problems

- [Decode Ways](../decode_ways/PROBLEM.md) — Next in category
- [Longest Palindromic Substring](../longest_palindromic_substring/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
