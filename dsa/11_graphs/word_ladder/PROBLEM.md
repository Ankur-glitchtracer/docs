---
impact: "High"
nr: false
confidence: 3
---
# 🪜 Graph: Word Ladder

## 📝 Problem Description
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:
- Every adjacent pair of words differs by exactly one letter.
- Every `si` for $1 \le i \le k$ is in `wordList`.
- `sk == endWord`.
Return the number of words in the shortest transformation sequence, or 0 if no such sequence exists.

!!! info "Real-World Application"
    This problem models **pathfinding in semantic networks** or state-space search where each word represents a state and a one-character change is an edge. It is useful in natural language processing (NLP) for measuring word similarity and in recommendation systems for finding related items.

## 🛠️ Constraints & Edge Cases
- $1 \le$ length of beginWord $\le 10$
- $1 \le$ wordList.length $\le 5000$
- **Edge Cases to Watch:** 
    - `endWord` not in `wordList`.
    - No transformation path exists.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Instead of comparing every word with every other word to check if they differ by one character ($O(N^2 \cdot L)$), use **generic patterns** (e.g., `h*t` for `hot`, `dot`, `lot`) as intermediary nodes in the graph. This reduces the edge-building process significantly.

### 🐢 Brute Force (Naive)
Creating an adjacency matrix where an edge exists if words differ by one character is too slow due to the $O(N^2)$ comparisons.

### 🐇 Optimal Approach
1. Create a dictionary (adjacency list) where keys are generic patterns (e.g., `h*t`) and values are lists of words matching that pattern.
2. Perform BFS from `beginWord` to `endWord`.
3. At each step, generate all possible patterns for the current word to find all reachable neighbors in one character change.

### 🧩 Visual Tracing
```mermaid
graph LR
    HOT[hot] --> |h*t| H_T[Generic]
    H_T --> DOT[dot]
    DOT --> |d*t| D_T[Generic]
    D_T --> DOG[dog]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(M \times N^2)$ or $\mathcal{O}(M^2 \times N)$ depending on implementation (where $M$ is length of word, $N$ is number of words).
- **Space Complexity:** $\mathcal{O}(M^2 \times N)$ to store the pattern dictionary.

---

## 🎤 Interview Toolkit

- **Harder Variant:** Bidirectional BFS: Search from both `beginWord` and `endWord` simultaneously to drastically reduce the search space.
- **Alternative Data Structures:** The dictionary-based adjacency list is the core optimization here.

## 🔗 Related Problems
- [Shortest Path in Binary Matrix](../../05_binary_search/search_2d_matrix/PROBLEM.md) — Finding shortest paths.
- [Rotting Oranges](../rotting_oranges/PROBLEM.md) — Another level-order BFS problem.
