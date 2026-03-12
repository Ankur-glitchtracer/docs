#  🔄 Sliding Window: Longest Repeating Character Replacement

## 📝 Description
[LeetCode 424](https://leetcode.com/problems/longest-repeating-character-replacement/)
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- $s$ consists of standard ASCII characters.

## 🧠 The Engineering Story

**The Villain:** "The Invalid Window." Trying to expand a window indefinitely. But wait, we are only allowed `k` replacements. How do we know when to stop?

**The Hero:** "The Max Frequency Anchor." The key insight: The number of replacements needed = `Window Size` - `Count of Most Frequent Char`.

**The Plot:**

1. Maintain a frequency map for chars in the current window.
2. Track `max_f` (count of the most frequent char in the current window).
3. If `(right - left + 1) - max_f > k`, the window is invalid. Shrink it from the left.
4. Update `max_len` at every valid step.

**The Twist (Failure):** **The Shrinking Max.** When you shrink the window, `max_f` might decrease. Surprisingly, you *don't* need to update `max_f` immediately because a smaller `max_f` won't produce a *better* result than what you've already found.

**Interview Signal:** Optimization logic in **Sliding Windows**.

## 🚀 Approach & Intuition
Valid window condition: `window_len - max_count <= k`.

### C++ Pseudo-Code
```cpp
int characterReplacement(string s, int k) {
    vector<int> count(26, 0);
    int l = 0, res = 0, maxf = 0;
    
    for (int r = 0; r < s.length(); r++) {
        count[s[r] - 'A']++;
        maxf = max(maxf, count[s[r] - 'A']);
        
        if ((r - l + 1) - maxf > k) {
            count[s[l] - 'A']--;
            l++;
        }
        res = max(res, r - l + 1);
    }
    return res;
}
```

### Key Observations:

- Maintain a window that satisfies a certain condition and expand/contract it as you iterate.
- Use a Hash Map or Frequency Array to track elements within the current window in $O(1)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (26 uppercase letters)

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

- [Permutation in String](../permutation_in_string/PROBLEM.md) — Next in category
- [Longest Substring No Repeat](../longest_substring_without_repeating_characters/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
