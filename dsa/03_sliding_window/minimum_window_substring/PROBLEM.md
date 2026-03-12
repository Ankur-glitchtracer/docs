#  🤏 Sliding Window: Minimum Window Substring

## 📝 Description
[LeetCode 76](https://leetcode.com/problems/minimum-window-substring/)
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string "".

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- $s$ consists of standard ASCII characters.

## 🧠 The Engineering Story

**The Villain:** "The Expansionist." Finding *a* valid window is easy. Finding the *minimum* one is hard. You expand until valid, but then what?

**The Hero:** "The Expand-Shrink Accordion."

**The Plot:**

1. **Expand (`right`):** Add characters until the window has all required chars from `t`.
2. **Valid State:** Use a variable `have` vs `need` to track validity in $O(1)$.
3. **Shrink (`left`):** Once valid, try to remove characters from the left to minimize length.
   - If removing a char breaks validity, stop shrinking and go back to expanding.
   - Keep track of the minimum window seen so far.

**The Twist (Failure):** **The Exact Count.** If `t` needs two 'A's, your window can have three. It's still valid. You only break validity when the count drops *below* the requirement.

**Interview Signal:** Handling **Dynamic Sliding Windows** with complex validity conditions.

## 🚀 Approach & Intuition
Expand right until valid, then shrink left to minimize.

### C++ Pseudo-Code
```cpp
string minWindow(string s, string t) {
    if (t == "") return "";
    unordered_map<char, int> countT, window;
    for (char c : t) countT[c]++;
    
    int have = 0, need = countT.size();
    int res[2] = {-1, -1}, resLen = INT_MAX;
    int l = 0;
    
    for (int r = 0; r < s.length(); r++) {
        char c = s[r];
        window[c]++;
        if (countT.count(c) && window[c] == countT[c]) have++;
        
        while (have == need) {
            if (r - l + 1 < resLen) {
                res[0] = l;
                res[1] = r;
                resLen = r - l + 1;
            }
            window[s[l]]--;
            if (countT.count(s[l]) && window[s[l]] < countT[s[l]]) have--;
            l++;
        }
    }
    return resLen == INT_MAX ? "" : s.substr(res[0], resLen);
}
```

### Key Observations:

- Maintain a window that satisfies a certain condition and expand/contract it as you iterate.
- Use a Hash Map or Frequency Array to track elements within the current window in $O(1)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (Size 128 array for ASCII)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the window size is not fixed, or we need to find the count of all windows satisfying a condition?
- **Scale Question:** In a streaming context (e.g., Flink or Spark Streaming), how would you maintain the window state efficiently?
- **Edge Case Probe:** How do you handle cases where no window satisfies the condition? What about very small inputs?

## 🔗 Related Problems

- [Sliding Window Maximum](../sliding_window_maximum/PROBLEM.md) — Next in category
- [Permutation in String](../permutation_in_string/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
