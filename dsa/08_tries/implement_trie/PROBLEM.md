---
impact: "High"
nr: false
confidence: 5
---
# 🌳 Tries: Implement Trie (Prefix Tree)

## 📝 Problem Description
Implement a `Trie` class with `insert`, `search`, and `startsWith` methods.

!!! info "Real-World Application"
    Tries are the backbone of modern text processing:
    - **Autocomplete:** Efficiently suggesting word completions.
    - **Spell Checkers:** Storing dictionaries for rapid word validation.
    - **IP Routing:** Longest prefix matching in network routers.

## 🛠️ Constraints & Edge Cases
- $1 \le \text{word.length} \le 2000$
- Words consist of lowercase English letters.
- **Edge Cases to Watch:** 
    - Inserting empty strings.
    - Searching prefixes that don't exist.
    - Repeated insertion of the same word.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Instead of storing strings directly, represent the dataset as a tree of characters where each node holds a map/array of its children. This allows for $O(L)$ lookups regardless of the number of strings in the trie.

### 🐢 Brute Force (Naive)
Storing all words in an array or a standard `HashSet`. Checking if a word exists is $O(L)$, but checking if a prefix exists requires scanning all strings ($O(N \cdot L)$), leading to Time Limit Exceeded for large dictionaries.

### 🐇 Optimal Approach
Use a tree structure where each node represents a character.
1. `TrieNode`: Contains a hash map of children nodes and a boolean `is_end`.
2. `insert`: Iterate through characters, creating nodes as needed. Mark last as `is_end`.
3. `search`: Traverse down; if any path is missing, return `false`. Return `is_end` at the target node.
4. `startsWith`: Same as search, but return `true` immediately after the loop.

### 🧩 Visual Tracing
```mermaid
graph TD
    Root((root)) -->|a| A((a))
    A -->|p| P1((p))
    P1 -->|p| P2((p))
    P2 -->|l| L((l))
    L -->|e| E((e))
    style E fill:#ccf,stroke:#333
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(L)$ where $L$ is the length of the string, for all operations.
- **Space Complexity:** $\mathcal{O}(N \cdot L)$ in the worst case (where no words share prefixes), where $N$ is the number of words.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Use compressed Tries (Radix Tree) if memory is tight and strings are long.
- **Alternative Data Structures:** Hash Map (good for search, bad for prefix matching).

## 🔗 Related Problems
- [Add and Search Words](../design_add_and_search_words_data_structure/PROBLEM.md) — Extension of basic Trie.
- [Word Search II](../word_search_ii/PROBLEM.md) — Advanced Trie usage with Backtracking.
