---
impact: "Hard"
nr: false
confidence: 2
---
# 🏊 Advanced Graph: Swim in Rising Water

## 📝 Description
[LeetCode 778](https://leetcode.com/problems/swim-in-rising-water/)
You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`. The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Return the least time until you can reach the bottom right square `(n - 1, n - 1)` if you start at the top left square `(0, 0)`.

!!! info "Real-World Application"
    This models **Pathfinding with Bottleneck Constraints**, such as finding a route for a vehicle that can only traverse terrain below a certain height, or network routing where links have varying bandwidths and you need the path with the best "minimum bandwidth".

## 🛠️ Constraints & Edge Cases
- $n \le 50$
- $0 \le grid[i][j] < n^2$
- **Edge Cases to Watch:**
    - `n=1` (Time is just `grid[0][0]`).
    - Start or End points have high elevation.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    This isn't just "shortest path" (fewest steps). It's "minimax path" (path minimizing the maximum edge weight). The "cost" to reach a neighbor is `max(current_time, neighbor_elevation)`. Since edge weights are non-negative, **Dijkstra's Algorithm** works perfectly. We prioritize visiting cells with the lowest required water level.

### 🐢 Brute Force (Naive)
Binary Search on the answer `T`. For a fixed `T`, run BFS/DFS to see if a path exists.
- **Time Complexity:** $O(N^2 \log (\text{max\_val}))$. Valid, but Dijkstra is often cleaner.

### 🐇 Optimal Approach (Dijkstra)
1.  Min-Heap stores `(time, r, c)`.
2.  Start: Push `(grid[0][0], 0, 0)`. Mark visited.
3.  While heap:
    - Pop `(t, r, c)`.
    - If `(r, c) == (N-1, N-1)`, return `t`.
    - For neighbors:
        - New time `new_t = max(t, grid[nr][nc])`.
        - If not visited, push `(new_t, nr, nc)` and mark visited.

### 🧩 Visual Tracing
```mermaid
graph TD
    Start[0,0: Val 3] -->|Heap: 3| Pop3
    Pop3 -->|Neigh 0,1: Val 2| Push3_2[Heap: (3, 0,1)]
    Pop3 -->|Neigh 1,0: Val 10| Push10[Heap: (3,0,1), (10,1,0)]
    Push3_2 -->|Pop 3| Next...
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N^2 \log N)$ — $N^2$ nodes, heap operations take log.
- **Space Complexity:** $\mathcal{O}(N^2)$ — Visited set and Heap.

---

## 🎤 Interview Toolkit

- **Alternative:** Kruskal's Algorithm (Union-Find). Sort all grid cells by value. Iterate and unite neighbors. Stop when Start connected to End.
- **Comparison:** Dijkstra is easier to implement here than Union-Find.

## 🔗 Related Problems
- [Network Delay Time](../network_delay_time/PROBLEM.md) — Standard Dijkstra
