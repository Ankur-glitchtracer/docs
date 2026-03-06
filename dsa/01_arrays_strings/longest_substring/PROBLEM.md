# 🪟 Strings: Longest Substring Without Repeating Characters

## 📝 Description
[LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
Given a string `s`, find the length of the longest substring without repeating characters.

## 🚀 Approach 1: Brute Force
Check every possible substring and verify if it contains unique characters.

### C++ Pseudo-Code
```cpp
int lengthOfLongestSubstring(string s) {
    int maxLen = 0;
    for (int i = 0; i < s.length(); i++) {
        for (int j = i; j < s.length(); j++) {
            if (isUnique(s, i, j)) {
                maxLen = max(maxLen, j - i + 1);
            }
        }
    }
    return maxLen;
}
```

!!! info "Analysis"
    - **Time:** $O(N^3)$ - $N^2$ substrings, each taking $O(N)$ to verify.
    - **Space:** $O(1)$ or $O(K)$ for character set check.

---

## 🚀 Approach 2: Sliding Window (Set) - **Optimal**
Use a sliding window defined by two pointers `left` and `right`. Expand `right` and if a duplicate is found, shrink `left` until the window is unique again.

### C++ Pseudo-Code
```cpp
int lengthOfLongestSubstring(string s) {
    unordered_set<char> seen;
    int left = 0, maxLen = 0;
    for (int right = 0; right < s.length(); right++) {
        while (seen.count(s[right])) {
            seen.erase(s[left]);
            left++;
        }
        seen.insert(s[right]);
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}
```

!!! success "Analysis"
    - **Time:** $O(N)$ - Each character is processed at most twice (once by each pointer).
    - **Space:** $O(\min(M, N))$ - $M$ is charset size.
