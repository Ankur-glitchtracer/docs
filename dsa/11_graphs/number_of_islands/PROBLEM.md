#  🏝️ Graphs: Number of Islands

## 📝 Description
[LeetCode 200](https://leetcode.com/problems/number-of-islands/)
Given an `m x n` 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

## 🛠️ Requirements/Constraints

- $m == grid.length$
- $n == grid[i].length$
- $1 \le m, n \le 300$
- $grid[i][j]$ is '0' or '1'.

## 🧠 The Engineering Story

**The Villain:** "The Fragmented Map." A 2D grid where you need to identify connected clusters of "1"s. Simply counting "1"s counts individual tiles, not whole islands.

**The Hero:** "The DFS Sinkhole." Every time you find land, "sink" the entire island (turn it to "0") by recursively visiting all its connected land neighbors.

**The Plot:**

1. Iterate through the grid row by row.
2. If you hit '1':
   - Increment `island_count`.
   - Start a DFS (or BFS) to mark all connected '1's as '0' (visited).
3. Continue until the whole grid is processed.

**The Twist (Failure):** **The Grid Overflow.** Forgetting to check boundaries before recursing, or failing to handle the "empty grid" edge case.

**Interview Signal:** Mastery of **Grid Traversal** and **Connected Components** in graphs.

## 🚀 Approach & Intuition
The problem asks us to find the number of connected components in a 2D grid. We can treat the grid as a graph where each '1' is a node connected to its horizontal and vertical neighbors. When we encounter land, we trigger a traversal (DFS or BFS) to "claim" all parts of that island so we don't count them again.

### Key Observations:

- We can modify the grid in-place to save space (by "sinking" the island).
- Each DFS call explores one full island.
- Boundary checks are crucial to avoid `IndexOutOfBounds`.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M \times N)$ where $M$ is rows and $N$ is columns. We visit each cell at most twice.
    - **Space Complexity:** $O(M \times N)$ in the worst case where the entire grid is land (for the recursion stack).

## 💻 Solution Implementation

```python
--8<-- "dsa/11_graphs/number_of_islands/solution.py"
```

!!! success "Aha! Moment"
    The key is "marking as visited." By turning '1's into '0's as we explore, we ensure that each island is only counted once, effectively "sinking" it into the ocean of processed data.

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you find the number of distinct island shapes? (See Number of Distinct Islands).
- **Scale Question:** If the map is 1 million by 1 million, how would you use Union-Find with path compression to process it in tiles?
- **Edge Case Probe:** How does the algorithm handle a map that is all water? What if the entire map is one big island?

## 🔗 Related Problems

- [Max Area of Island](../max_area_of_island/PROBLEM.md) — Next in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
