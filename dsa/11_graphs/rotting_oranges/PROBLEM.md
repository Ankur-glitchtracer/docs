#  🍊 Graph: Rotting Oranges

## 📝 Description
[LeetCode 994](https://leetcode.com/problems/rotting-oranges/)
You are given an `m x n` grid where each cell can have one of three values:

- `0`: representing an empty cell,
- `1`: representing a fresh orange, or
- `2`: representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Ticking Clock." Oranges rot layer by layer every minute. We need to find how many minutes until all possible oranges rot.

**The Hero:** "The Level-Order Simulation." This is effectively Multi-Source BFS, where each "level" represents one minute.

**The Plot:**

1. Count fresh oranges (`fresh_cnt`) and queue up all initially rotten ones.
2. If `fresh_cnt == 0`, return 0.
3. BFS Loop:
   - Increment `minutes`.
   - Process **current queue size** (all oranges rotting at this specific minute).
   - Infect neighbors: Decrement `fresh_cnt`, Add to queue.
4. If `fresh_cnt == 0` after loops, return `minutes`. Else return -1.

**The Twist (Failure):** **The Extra Minute.** The loop increments time even for the last layer when no *new* neighbors are infected. You usually return `minutes - 1` or check if the queue is non-empty before incrementing.

**Interview Signal:** BFS for **Shortest Path / Propagation** in unweighted graphs.

## 🚀 Approach & Intuition
Track time levels.

### C++ Pseudo-Code
```cpp
int orangesRotting(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    queue<pair<int, int>> q;
    int fresh = 0;
    
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (grid[r][c] == 2) q.push({r, c});
            else if (grid[r][c] == 1) fresh++;
        }
    }
    
    if (fresh == 0) return 0;
    int minutes = 0;
    int dirs[] = {0, 1, 0, -1, 0};
    
    while (!q.empty() && fresh > 0) {
        minutes++;
        int size = q.size();
        while (size--) {
            auto [r, c] = q.front(); q.pop();
            for (int i = 0; i < 4; i++) {
                int nr = r + dirs[i], nc = c + dirs[i+1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    fresh--;
                    q.push({nr, nc});
                }
            }
        }
    }
    return fresh == 0 ? minutes : -1;
}
```

### Key Observations:

- Represent the graph using an Adjacency List for space efficiency in sparse graphs.
- Use DFS for path-finding/connectivity and BFS for finding the shortest path in unweighted graphs.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M 	imes N)$
    - **Space Complexity:** $O(M 	imes N)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you solve this using BFS for shortest paths or DFS for connectivity? When would you use Union-Find?
- **Scale Question:** If the graph has billions of edges (like a social network), how would you use a Pregel or Giraph-style distributed processing model?
- **Edge Case Probe:** How do you handle cycles, disconnected components, or self-loops in the graph?

## 🔗 Related Problems

- [Pacific Atlantic Water Flow](../pacific_atlantic_water_flow/PROBLEM.md) — Next in category
- [Walls and Gates](../walls_and_gates/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
