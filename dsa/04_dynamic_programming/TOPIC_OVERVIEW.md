# 📉 Topic Overview: Dynamic Programming

DP is an optimization technique. It solves problems by breaking them down into simpler subproblems and storing their solutions (Memoization/Tabulation).

## 🔑 Key Concepts Checklist
- [ ] **Top-Down (Memoization):** Recursion + Caching. Easier to write, good for sparse state spaces.
- [ ] **Bottom-Up (Tabulation):** Iteration + Table filling. No recursion overhead, can optimize space.
- [ ] **State Definition:** Identifying what variables uniquely define a subproblem (e.g., `dp[i]`, `dp[i][j]`).
- [ ] **Transition Relation:** The recurrence formula connecting subproblems.

## 🎯 Essential Problem Checklist (95% Coverage)
| Problem | Pattern | Difficulty |
| :--- | :--- | :--- |
| **Climbing Stairs** | 1D DP (Fibonacci) | Easy |
| **House Robber** | 1D DP | Medium |
| **Coin Change** | Unbounded Knapsack | Medium |
| **Longest Increasing Subsequence** | 1D DP ($O(N^2)$ vs $O(N \log N)$) | Medium |
| **Longest Common Subsequence** | 2D DP (String matching) | Medium |
| **0/1 Knapsack** | 2D DP (Standard) | Medium |
| **Edit Distance** | 2D DP (Strings) | Hard |
| **Unique Paths** | 2D DP (Grid) | Medium |
| **Burst Balloons** | Interval DP | Hard |
| **Traveling Salesperson** | Bitmask DP | Hard |

## ⏱️ Complexity Cheatsheet
| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| Brute Force (Recursion) | Exponential ($O(2^N)$) | $O(N)$ (Stack) |
| Memoization (Top-Down) | $O(N \times \text{States})$ | $O(N \times \text{States})$ |
| Tabulation (Bottom-Up) | $O(N \times \text{States})$ | $O(N \times \text{States})$ |
| Space Optimized | $O(N \times \text{States})$ | $O(1)$ or $O(N)$ (Row only) |

## 📚 Recommended Reading (CP-Algorithms)
- [Dynamic Programming - Introduction](https://cp-algorithms.com/dynamic_programming/intro.html)
- [0/1 Knapsack & Variatons](https://cp-algorithms.com/dynamic_programming/knapsack.html)
- [Longest Increasing Subsequence (LIS)](https://cp-algorithms.com/sequences/lis.html)
- [Edit Distance / Levenshtein](https://cp-algorithms.com/string/main.html#string-edit-distance)
- [Bitmask DP (Traveling Salesperson)](https://cp-algorithms.com/dynamic_programming/profile-dp.html)

## 🔗 External References
- [Dynamic Programming Patterns (LeetCode Discuss)](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
- [MIT 6.006: Dynamic Programming I](https://www.youtube.com/watch?v=OQ5dgkfKW9U)
