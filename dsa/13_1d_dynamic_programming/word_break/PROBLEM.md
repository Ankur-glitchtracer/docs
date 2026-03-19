---
impact: "Medium"
nr: false
confidence: 4
---
# 📖 DP: Word Break

## 📝 Problem Description
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words. Dictionary words can be reused.

!!! info "Real-World Application"
    Fundamental in Natural Language Processing (NLP), such as in tokenization for languages without spaces (e.g., Chinese, Japanese) or correcting spelling in search engines.

## 🛠️ Constraints & Edge Cases
- $1 \le \text{s.length} \le 300$
- $1 \le \text{wordDict.length} \le 1000$
- **Edge Cases:** Empty dictionary, string cannot be segmented, dictionary contains all substrings.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    We don't need to backtrack. If we know `s[0:j]` can be segmented (let this be `dp[j]`), then `s[0:i]` can be segmented if `s[j:i]` is in the dictionary. We define `dp[i]` as a boolean: can the prefix of length `i` be broken into words?

### 🐢 Brute Force (Naive)
Generating all possible ways to partition the string takes exponential time $\mathcal{O}(2^N)$ because we explore every split point.

### 🐇 Optimal Approach
Use bottom-up DP:
1. Initialize a boolean array `dp` of size `n+1`, where `dp[0] = True` (empty string).
2. For each length `i` from $1$ to `n`:
   - Iterate through all possible split points `j < i`.
   - If `dp[j]` is `True` and `s[j:i]` is in the `wordSet`, set `dp[i] = True` and break the inner loop.
3. Return `dp[n]`.

### 🧩 Visual Tracing
```mermaid
graph LR
    S[s = applepenapple] --> D1[dp[0]=T]
    D1 -- "apple" --> D2[dp[5]=T]
    D2 -- "pen" --> D3[dp[8]=T]
    D3 -- "apple" --> D4[dp[13]=T]
    style D4 fill:#cfc,stroke:#333,stroke-width:2px
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N^3)$ — Outer loops are $\mathcal{O}(N^2)$, and string slicing/hashing in the inner loop takes $\mathcal{O}(N)$.
- **Space Complexity:** $\mathcal{O}(N)$ — We store the `dp` array of size `n+1`.

---

## 🎤 Interview Toolkit

- **Harder Variant:** If you need to return all possible sentences (not just boolean), this becomes a backtracking problem (Word Break II).
- **Alternative Data Structures:** Using a Trie to store the dictionary can speed up substring lookups if the dictionary is extremely large.

## 🔗 Related Problems
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — 2D DP application.
- [Longest Increasing Subsequence](../longest_increasing_subsequence/PROBLEM.md) — Another partitioning/linear DP problem.
