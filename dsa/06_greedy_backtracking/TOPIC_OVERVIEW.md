# 💡 Topic Overview: Greedy & Backtracking

Greedy makes the best local choice, while Backtracking explores all potential paths by undoing choices that lead to dead ends.

## 🔑 Key Concepts Checklist
- [ ] **Greedy Choice Property:** A global optimum can be reached by choosing a local optimum.
- [ ] **Optimal Substructure:** A problem can be solved by combining solutions to subproblems.
- [ ] **State Space Tree:** Visualizing the paths in backtracking.
- [ ] **Pruning:** Discarding branches of the tree that cannot lead to a solution.

## 🎯 Essential Problem Checklist (95% Coverage)
| Problem | Key Concept | Difficulty |
| :--- | :--- | :--- |
| **Subsets** | Backtracking (Include/Exclude) | Medium |
| **Permutations** | Backtracking (Swap/Visited) | Medium |
| **N-Queens** | Backtracking (Constraint pruning) | Hard |
| **Sudoku Solver** | Backtracking | Hard |
| **Activity Selection** | Greedy (Sort by end time) | Easy |
| **Gas Station** | Greedy (One pass) | Medium |
| **Jump Game** | Greedy (Max reach) | Medium |
| **Word Search** | Backtracking + DFS | Medium |

## 🚀 Key Pattern: Backtracking Template
```cpp
void backtrack(State& curr, Choices& choices) {
    if (isSolution(curr)) {
        processSolution(curr);
        return;
    }
    for (auto choice : choices) {
        if (isValid(choice)) {
            makeChoice(curr, choice);   // Do
            backtrack(curr, choices);   // Recurse
            undoChoice(curr, choice);   // Undo (Backtrack)
        }
    }
}
```

## 📚 Recommended Reading (CP-Algorithms)
<!-- - [Greedy Algorithms](https://cp-algorithms.com/others/maximum_subarray_sum.html) (Logic overlaps) -->
- [Search subarray with maximum/minimum sum](https://cp-algorithms.com/others/maximum_average_segment.html)
- [Gauss method for solving system  of linear equations](https://cp-algorithms.com/linear_algebra/linear-system-gauss.html)
<!-- - [Heuristics](https://cp-algorithms.com/others/randomized_algorithms.html) -->
