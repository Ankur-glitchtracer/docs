---
impact: "Medium"
nr: false
confidence: 3
---
# 🧩 Greedy: Partition Labels

## 📝 Problem Description
You are given a string `s`. You want to partition the string into as many parts as possible such that each letter appears in at most one part. Return a list of integers representing the sizes of these parts.

!!! info "Real-World Application"
    Used in streaming data architectures or text processing to identify independent processing windows where characters (or tokens) don't overlap across boundaries.

## 🛠️ Constraints & Edge Cases
- $1 \le s.length \le 500$
- `s` consists of lowercase English letters.
- **Edge Cases to Watch:** 
    - String with one character.
    - String where all characters are distinct.
    - String where all characters are the same.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    To ensure a character appears in only one partition, we must extend the current partition boundary to the *last* occurrence of any character currently included in the partition.

### 🐢 Brute Force (Naive)
Trying all possible split points recursively would involve $\mathcal{O}(2^N)$ complexity, which is inefficient.

### 🐇 Optimal Approach
1. Record the last occurrence index of every character in a hash map.
2. Iterate through the string, maintaining `start` and `end` pointers for the current partition.
3. Update `end` to `max(end, last_index[current_char])`.
4. If the current index reaches `end`, a partition is found. Record its length, update `start` to `i + 1`.

### 🧩 Visual Tracing
```mermaid
graph LR
    S[Start] -- Extend to Last Occur --> E[End]
    E -- If i == End --> P[Partition Found]
    P --> S2[New Start]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ — We traverse the string twice (once to map indices, once to partition).
- **Space Complexity:** $\mathcal{O}(1)$ — Since the alphabet size is constant (26 letters).

---

## 🎤 Interview Toolkit

- **Harder Variant:** What if we had a stream of characters where the total number of characters isn't known upfront?
- **Alternative Data Structures:** Simple hash map suffices.

## 🔗 Related Problems
- [Merge Triplets](../merge_triplets_to_form_target_triplet/PROBLEM.md)
- [Jump Game II](../jump_game_ii/PROBLEM.md)
