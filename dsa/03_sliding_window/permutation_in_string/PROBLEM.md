#  🔀 Sliding Window: Permutation in String

## 📝 Description
[LeetCode 567](https://leetcode.com/problems/permutation-in-string/)
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise. In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- $s$ consists of standard ASCII characters.

## 🧠 The Engineering Story

**The Villain:** "The Substring Generator." Checking every substring of `s2` and sorting it to compare with sorted `s1` ($O(N \cdot M \log M)$).

**The Hero:** "The Fixed-Size Window." Since the substring must be the same length as `s1`, we slide a window of size `len(s1)` across `s2`.

**The Plot:**

1. Create frequency arrays for `s1` and the first window of `s2`.
2. Check if they match.
3. Slide the window one step right:
   - Add the new character to the count.
   - Remove the old character (left of window) from the count.
   - Check match again.

**The Twist (Failure):** **The Comparison Cost.** Comparing two arrays of size 26 takes constant time $O(26) = O(1)$. Don't use a full hash map if you can use an array.

**Interview Signal:** Fixed-size **Sliding Window** management.

## 🚀 Approach & Intuition
Compare character counts in a window of size `s1.length()`.

### C++ Pseudo-Code
```cpp
bool checkInclusion(string s1, string s2) {
    if (s1.length() > s2.length()) return false;
    vector<int> s1map(26, 0), s2map(26, 0);
    
    for (int i = 0; i < s1.length(); i++) {
        s1map[s1[i] - 'a']++;
        s2map[s2[i] - 'a']++;
    }
    
    int matches = 0;
    for (int i = 0; i < 26; i++) 
        if (s1map[i] == s2map[i]) matches++;
        
    int l = 0;
    for (int r = s1.length(); r < s2.length(); r++) {
        if (matches == 26) return true;
        
        int index = s2[r] - 'a';
        s2map[index]++;
        if (s1map[index] == s2map[index]) matches++;
        else if (s1map[index] + 1 == s2map[index]) matches--;
        
        index = s2[l] - 'a';
        s2map[index]--;
        if (s1map[index] == s2map[index]) matches++;
        else if (s1map[index] - 1 == s2map[index]) matches--;
        l++;
    }
    return matches == 26;
}
```

### Key Observations:

- Maintain a window that satisfies a certain condition and expand/contract it as you iterate.
- Use a Hash Map or Frequency Array to track elements within the current window in $O(1)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (Size 26 arrays)

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

- [Minimum Window Substring](../minimum_window_substring/PROBLEM.md) — Next in category
- [Longest Repeating Replacement](../longest_repeating_character_replacement/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
