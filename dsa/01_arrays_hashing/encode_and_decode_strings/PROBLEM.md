#  🔒 Arrays & Hashing: Encode and Decode Strings

## 📝 Description
[LeetCode 271](https://leetcode.com/problems/encode-and-decode-strings/)
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^9 \le nums[i] \le 10^9$

## 🧠 The Engineering Story

**The Villain:** "The Delimiter Collision." You decide to join strings with a `#` (e.g., `apple#banana`). But what if the input string itself contains a `#`? The decoder will break.

**The Hero:** "The Length-Prefix Protocol." Before the content, explicitly state how long the content is.

**The Plot:**

1. **Encode:** For each string, format it as `length + delimiter + content`. E.g., `(To be detailed...)` -> `"5#hello5#world"`.
2. **Decode:** Read the digits until the delimiter to get `length`. Then read exactly `length` characters. Repeat.

**The Twist (Failure):** **The Multi-Digit Length.** Handling lengths like `12` or `100`. You must read *all* digits before the delimiter, not just one.

**Interview Signal:** Understanding of **Serialization/Deserialization** principles.

## 🚀 Approach & Intuition
Prefix each string with its length and a delimiter (e.g., `4#Code`).

### C++ Pseudo-Code
```cpp
string encode(vector<string>& strs) {
    string res = "";
    for (string s : strs) {
        res += to_string(s.length()) + "#" + s;
    }
    return res;
}

vector<string> decode(string s) {
    vector<string> res;
    int i = 0;
    while (i < s.length()) {
        int j = i;
        while (s[j] != '#') j++;
        int len = stoi(s.substr(i, j - i));
        res.push_back(s.substr(j + 1, len));
        i = j + 1 + len;
    }
    return res;
}
```

### Key Observations:

- Hash Maps and Hash Sets are the primary tools for achieving $O(N)$ time complexity by trading space.
- Consider if sorting the array ($O(N \log N)$) simplifies the problem or allows for $O(1)$ space.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ (Total characters)
    - **Space Complexity:** $O(N)$

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

- [Longest Consecutive Sequence](../longest_consecutive_sequence/PROBLEM.md) — Next in category
- [Valid Sudoku](../valid_sudoku/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
