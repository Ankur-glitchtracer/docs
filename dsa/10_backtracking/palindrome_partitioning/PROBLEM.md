#  🪞 Backtracking: Palindrome Partitioning

## 📝 Description
[LeetCode 131](https://leetcode.com/problems/palindrome-partitioning/)
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Valid Split." How do you split "aab" into valid palindromes? "a", "a", "b"? "aa", "b"? Checking every possible cut location recursively.

**The Hero:** "The DFS Cutter." Try to cut at index `i`. Is `s[start...i]` a palindrome?

**The Plot:**

1. Iterate `i` from `start` to end.
2. Check `isPalindrome(s, start, i)`.
3. If yes:
   - Add substring to `current_partition`.
   - Recurse for `i + 1`.
   - Backtrack (remove substring).
4. Base Case: `start == s.length` -> Add partition to results.

**The Twist (Failure):** **Repeated Checks.** `isPalindrome` checks the same substrings repeatedly. Optimization: Use DP to precompute a palindrome table `dp[i][j]`.

**Interview Signal:** Backtracking combined with **String Validation**.

## 🚀 Approach & Intuition
Try every valid prefix palindrome and recurse.

### C++ Pseudo-Code
```cpp
vector<vector<string>> partition(string s) {
    vector<vector<string>> res;
    vector<string> curr;
    
    function<bool(int, int)> isPali = [&](int l, int r) {
        while (l < r) if (s[l++] != s[r--]) return false;
        return true;
    };
    
    function<void(int)> backtrack = [&](int start) {
        if (start == s.length()) {
            res.push_back(curr);
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (isPali(start, i)) {
                curr.push_back(s.substr(start, i - start + 1));
                backtrack(i + 1);
                curr.pop_back();
            }
        }
    };
    
    backtrack(0);
    return res;
}
```

### Key Observations:

- Backtracking is essentially a DFS on a state-space tree where we 'undo' the last move to explore other branches.
- Pruning is the most important optimization to skip branches that cannot lead to a valid solution.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot 2^N)$
    - **Space Complexity:** $O(N)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you use Pruning or Bitmasking to significantly reduce the search space?
- **Scale Question:** How would you parallelize the search? Would you use Work Stealing to balance the load between threads?
- **Edge Case Probe:** What is the maximum depth of recursion before you hit a stack overflow?

## 🔗 Related Problems

- [Letter Combinations](../letter_combinations_of_a_phone_number/PROBLEM.md) — Next in category
- [Word Search](../word_search/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
