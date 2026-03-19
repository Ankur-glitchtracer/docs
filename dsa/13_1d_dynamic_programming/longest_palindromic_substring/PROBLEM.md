---
impact: "Medium"
nr: false
confidence: 4
---
# 🎀 DP: Longest Palindromic Substring

## 📝 Problem Description
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same forwards and backwards.

!!! info "Real-World Application"
    This algorithm is used in bioinformatics for DNA sequence analysis (finding symmetrical patterns in sequences) and in text compression tools to identify repeating patterns.

## 🛠️ Constraints & Edge Cases
- $1 \le \text{s.length} \le 1000$
- `s` consists of only digits and English letters.
- **Edge Cases to Watch:** 
    - Empty string (return "")
    - Single character (return the character)
    - All characters are the same (return the whole string)

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Instead of building a DP table, treat each character (or gap between characters) as a potential center of a palindrome and expand outwards until the palindrome property is violated.

### 🐢 Brute Force (Naive)
Checking every possible substring and verifying if it's a palindrome takes $\mathcal{O}(N^3)$, which is inefficient for $N=1000$.

### 🐇 Optimal Approach
For each possible center ($2N-1$ total centers), expand outwards as long as characters match.

### 🧩 Visual Tracing
```mermaid
graph LR
    A[aba] --> B[Center: b]
    B --> C[Expand: a == a]
    C --> D[Result: aba]
    style C fill:#f9f,stroke:#333
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N^2)$ — We have $2N$ centers, and expansion takes $\mathcal{O}(N)$.
- **Space Complexity:** $\mathcal{O}(1)$ — No extra space is required for the expansion logic (excluding output).

---

## 🎤 Interview Toolkit

- **Harder Variant:** Manacher's Algorithm can solve this in $\mathcal{O}(N)$ time.
- **Alternative Data Structures:** Can be solved with a Trie or Suffix Tree if querying for multiple palindromes is required.

## 🔗 Related Problems
- [Palindromic Substrings](../palindromic_substrings/PROBLEM.md) — Related counting problem.
