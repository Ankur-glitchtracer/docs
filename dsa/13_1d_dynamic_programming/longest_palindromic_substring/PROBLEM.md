#  🪞 DP: Longest Palindromic Substring

## 📝 Description
[LeetCode 5](https://leetcode.com/problems/longest-palindromic-substring/)
Given a string `s`, return the longest palindromic substring in `s`.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Middle-Out Challenge." A palindrome mirrors around a center. Checking all substrings is $O(N^3)$.

**The Hero:** "The Center Expansion." Iterate through every character (and every gap between characters) and treat it as the center. Expand outwards while `left == right`.

**The Plot:**

1. Iterate `i` from 0 to `n`.
2. Expand for odd length: `l=i, r=i`.
3. Expand for even length: `l=i, r=i+1`.
4. Keep track of `max_len` and `start_index`.
5. Return substring.

**The Twist (Failure):** **The Even Case.** Forgetting that palindromes can be even length (`abba` centers between `b` and `b`).

**Interview Signal:** Optimization from $O(N^3)$ to $O(N^2)$ without extra space.

## 🚀 Approach & Intuition
Treat every character (and gap) as a potential center.

### C++ Pseudo-Code
```cpp
string longestPalindrome(string s) {
    int resLen = 0, resStart = 0;
    
    for (int i = 0; i < s.length(); i++) {
        // Odd length
        int l = i, r = i;
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            if (r - l + 1 > resLen) {
                resStart = l;
                resLen = r - l + 1;
            }
            l--; r++;
        }
        
        // Even length
        l = i; r = i + 1;
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            if (r - l + 1 > resLen) {
                resStart = l;
                resLen = r - l + 1;
            }
            l--; r++;
        }
    }
    return s.substr(resStart, resLen);
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

- [Palindromic Substrings](../palindromic_substrings/PROBLEM.md) — Next in category
- [House Robber II](../house_robber_ii/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
