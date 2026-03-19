---
impact: "Medium"
nr: false
confidence: 2
---
# 🌳 Trie: Design Add and Search Words Data Structure

## 📝 Description
[LeetCode 211](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
Design a data structure that supports adding new words and finding if a string matches any previously added string. The search string may contain dots '.' where a dot can be matched with any letter.

!!! info "Real-World Application"
    This simulates a **Spell Checker** with wildcard support or **File System Globbing** (e.g., searching for `*.txt`).

## 🛠️ Constraints & Edge Cases
- $1 \le \text{word.length} \le 25$
- At most $10^4$ calls.
- **Edge Cases to Watch:**
    - `.` at start, middle, or end.
    - Word containing all dots.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Standard Tries handle direct lookups easily. The dot `.` introduces branching. If we encounter `.`, we can't go down a single path—we must explore **all** existing children of the current node. This suggests a recursive DFS.

### 🐢 Brute Force (Naive)
Store list of words. For `.` search, iterate all words and regex match.
- **Time Complexity:** $O(N \cdot L)$ per search. Slow if many words.

### 🐇 Optimal Approach
1.  **Add:** Standard Trie insertion ($O(L)$).
2.  **Search:** Recursive `dfs(index, root)`.
3.  If char is letter: Move to specific child.
4.  If char is `.`: Loop through **all 26 children**. If any path returns True, return True.

### 🧩 Visual Tracing
```mermaid
graph TD
    Root --> B
    B --> A
    A --> D[bad (End)]
    Root -->|Search b.d| ScanChildren
    ScanChildren -->|Try 'a'| D
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $O(L)$ for add. $O(26^L)$ worst case for search (all dots), but much faster on average due to pruning.
- **Space Complexity:** $\mathcal{O}(N \cdot L)$ — Total characters stored.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Regex support (`*`, `?`). (LeetCode 10: Regular Expression Matching).

## 🔗 Related Problems
- [Word Search II](../word_search_ii/PROBLEM.md) — Next in category
- [Implement Trie](../implement_trie/PROBLEM.md) — Previous in category
