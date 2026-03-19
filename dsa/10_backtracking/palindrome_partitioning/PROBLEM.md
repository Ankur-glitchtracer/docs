---
impact: "Medium"
nr: false
confidence: 2
---
# 🪞 Backtracking: Palindrome Partitioning

## 📝 Description
[LeetCode 131](https://leetcode.com/problems/palindrome-partitioning/)
Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

!!! info "Real-World Application"
    Algorithms that decompose data into valid substructures, such as **Bioinformatics** (DNA palindromic cutting), **Text Segmentation** (segmenting Chinese text into words), or decomposing packets.

## 🛠️ Constraints & Edge Cases
- $1 \le s.length \le 16$
- **Edge Cases to Watch:**
    - Single character (Always a palindrome).
    - Entire string is palindrome.
    - No palindromes longer than 1 char (partition into individual chars).

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    This is a "cut" problem. We can make a cut at any index `i` if `s[0...i]` is a palindrome. Then we recursively solve for the rest of the string `s[i+1...]`. The "state" is just the starting index.

### 🐢 Brute Force (Naive)
Generate every possible partition (cut at every possible set of indices), then check if all parts are palindromes. $O(2^N \cdot N)$.

### 🐇 Optimal Approach (DFS)
1.  Define `dfs(i)`: partitions starting from index `i`.
2.  **Loop** `j` from `i` to `len(s)`:
    - Check if substring `s[i...j]` is a palindrome.
    - If YES:
        - Add `s[i...j]` to `current_part`.
        - Recurse `dfs(j + 1)`.
        - Backtrack (remove substring).
3.  **Base Case:** If `i >= len(s)`, add `current_part` to result.

### 🧩 Visual Tracing
```mermaid
graph TD
    Root[s: aab] -->|Cut 'a'| A1[s: ab]
    Root -->|Cut 'aa'| A2[s: b]
    A1 -->|Cut 'a'| B1[s: b]
    A1 -->|Cut 'ab' (No)| X
    B1 -->|Cut 'b'| C1[Done: [a, a, b]]
    A2 -->|Cut 'b'| C2[Done: [aa, b]]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(2^N \cdot N)$ — $2^N$ possible subsets/partitions, $N$ to check palindrome/copy.
- **Space Complexity:** $\mathcal{O}(N)$ — Recursion stack.

---

## 🎤 Interview Toolkit

- **Optimization:** Use Dynamic Programming (Table `dp[i][j]`) to check palindrome status in $O(1)$ instead of $O(N)$.
- **Harder Variant:** Palindrome Partitioning II (Minimum cuts required).

## 🔗 Related Problems
- [Word Break](../../13_1d_dynamic_programming/word_break/PROBLEM.md) — Similar DP/Backtracking structure
