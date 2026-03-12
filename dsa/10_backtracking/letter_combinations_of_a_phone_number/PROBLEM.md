#  📞 Backtracking: Letter Combinations of a Phone Number

## 📝 Description
[LeetCode 17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order. A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## 🛠️ Requirements/Constraints

- Input size is usually small ($N \le 20$) due to exponential complexity.
- All possible solutions must be returned.

## 🧠 The Engineering Story

**The Villain:** "The Mapping Explosion." '2' maps to "abc", '3' to "def". Input "23" means choosing one from {a,b,c} AND one from {d,e,f}.

**The Hero:** "The Recursive Builder."

**The Plot:**

1. Map digits to letters: `{'2': "abc", '3': "def"...}`.
2. Base Case: `index == digits.length`. Add `current_string` to result.
3. Recursive Step:
   - Get letters for `digits[index]`.
   - Loop through each letter.
   - Append to `current_string`.
   - Recurse `index + 1`.
   - Backtrack (remove last char).

**The Twist (Failure):** **Empty Input.** If input is empty string, return empty list, not `[""]`.

**Interview Signal:** Basic **combinatorial generation**.

## 🚀 Approach & Intuition
Iterate through possible letters for current digit.

### C++ Pseudo-Code
```cpp
vector<string> letterCombinations(string digits) {
    if (digits.empty()) return {};
    vector<string> res;
    string pad[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    function<void(int, string)> backtrack = [&](int i, string s) {
        if (i == digits.size()) {
            res.push_back(s);
            return;
        }
        for (char c : pad[digits[i] - '0']) {
            backtrack(i + 1, s + c);
        }
    };
    
    backtrack(0, "");
    return res;
}
```

### Key Observations:

- Backtracking is essentially a DFS on a state-space tree where we 'undo' the last move to explore other branches.
- Pruning is the most important optimization to skip branches that cannot lead to a valid solution.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(4^N \cdot N)$
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

- [N-Queens](../n_queens/PROBLEM.md) — Next in category
- [Palindrome Partitioning](../palindrome_partitioning/PROBLEM.md) — Previous in category
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite for Graphs
- [Climbing Stairs](../../13_1d_dynamic_programming/climbing_stairs/PROBLEM.md) — Prerequisite for 1-D Dynamic Programming
