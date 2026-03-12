#  📖 DP: Word Break

## 📝 Description
[LeetCode 139](https://leetcode.com/problems/word-break/)
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words. Note that the same word in the dictionary may be reused multiple times in the segmentation.

## 🛠️ Requirements/Constraints

- $1 \le n \le 1000$ (Problem size)
- Values fit within a 64-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Greedy Split." "applepenapple". Dictionary: (To be detailed...). If you greedily match "apple", you're left with "penapple". Works. But what if dict is (To be detailed...)? Greedily matching "app" leaves "lepen...", which might fail.

**The Hero:** "The Boolean DP." `dp[i]` is true if `s[0...i]` can be segmented.

**The Plot:**

1. `dp[0] = true` (Empty string is valid).
2. Iterate `i` from 1 to `n`.
3. Iterate `j` from 0 to `i`.
   - If `dp[j]` is true AND `s[j...i]` is in dict:
     - `dp[i] = true`.
     - Break (no need to check other `j`s).

**The Twist (Failure):** **Substring Check.** Checking `s[j...i]` in dict takes $O(L)$ or $O(1)$ with Hash Set. Total time $O(N^2)$.

**Interview Signal:** **Partitioning DP**.

## 🚀 Approach & Intuition
Check if prefix is valid + suffix is in dict.

### C++ Pseudo-Code
```cpp
bool wordBreak(string s, vector<string>& wordDict) {
    unordered_set<string> dict(wordDict.begin(), wordDict.end());
    int n = s.size();
    vector<bool> dp(n + 1, false);
    dp[0] = true;
    
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            if (dp[j] && dict.count(s.substr(j, i - j))) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}
```

### Key Observations:

- Break down the problem into smaller sub-problems and store their results to avoid redundant calculations.
- Determine the base cases and the recurrence relation; bottom-up (tabulation) is often more space-efficient.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2 \cdot M)$ or $O(N^3)$ depending on substring/hash cost.
    - **Space Complexity:** $O(N)$

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

- [Longest Increasing Subseq](../longest_increasing_subsequence/PROBLEM.md) — Next in category
- [Max Product Subarray](../maximum_product_subarray/PROBLEM.md) — Previous in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
