#  🔠 Arrays & Hashing: Valid Anagram

## 📝 Description
[LeetCode 242](https://leetcode.com/problems/valid-anagram/)
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## 🛠️ Requirements/Constraints

- $1 \le s.length, t.length \le 5 \cdot 10^4$
- $s$ and $t$ consist of lowercase English letters.

## 🧠 The Engineering Story

**The Villain:** "The Permutation Generator." Generating all possible rearrangements of string S to see if it matches string T ($O(N!)$). This is computationally impossible for long strings.

**The Hero:** "The Frequency Counter." Anagrams must have the exact same count of every character.

**The Plot:**

1. Check if lengths are different. If so, return `false`.
2. Use a hash map (or an array of size 26 for lowercase English letters) to count char frequencies in S.
3. Decrement frequencies using T.
4. If all counts return to zero, it's an anagram.

**The Twist (Failure):** **Unicode Support.** An array of 26 works for 'a-z', but fails for emojis or Chinese characters. A specialized Hash Map is needed for full Unicode support.

**Interview Signal:** Mastery of **Hash Maps for Frequency Counting**.

## 🚀 Approach & Intuition
Count characters in the first string and decrement for the second string.

### C++ Pseudo-Code
```cpp
bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;
    vector<int> count(26, 0);
    for (int i = 0; i < s.length(); i++) {
        count[s[i] - 'a']++;
        count[t[i] - 'a']--;
    }
    for (int c : count) {
        if (c != 0) return false;
    }
    return true;
}
```

### Key Observations:

- Sorting both strings ($O(N \log N)$) is a simple way to check for anagrams, but a frequency counter ($O(N)$) is faster.
- If the input is limited to lowercase English letters, a fixed-size array of 26 integers is more space-efficient than a hash map.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (since alphabet size is fixed at 26)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the inputs contain Unicode characters? (Use a hash map instead of a fixed-size array). How would you find all anagrams in a list of 1 million strings?
- **Scale Question:** If you have billions of strings, how would you use MapReduce to group all anagrams together?
- **Edge Case Probe:** Does your solution correctly handle empty strings or strings of different lengths immediately?

## 🔗 Related Problems

- [Two Sum](../two_sum/PROBLEM.md) — Next in category
- [Contains Duplicate](../contains_duplicate/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
