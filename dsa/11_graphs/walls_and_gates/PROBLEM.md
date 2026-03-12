#  🌊 Graph: Walls and Gates (Distance to Nearest 0)

## 📝 Description
[LeetCode 286](https://leetcode.com/problems/walls-and-gates/) (Premium) / Equivalent to "01 Matrix".
You are given an `m x n` grid rooms initialized with these three possible values.

- `-1`: A wall or an obstacle.
- `0`: A gate.
- `INF`: Infinity means an empty room.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with `INF`.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Repeated BFS." Launching a BFS from *every empty room* to find the nearest gate. If there are many empty rooms, you re-scan the grid repeatedly ($O(Rooms \cdot Grid)$).

**The Hero:** "The Multi-Source BFS." Start the BFS from **all gates simultaneously**.

**The Plot:**

1. Put all Gates (`0`) into the Queue.
2. Initialize distance `0`.
3. While Queue not empty:
   - Pop `(r, c)`.
   - For each neighbor `(nr, nc)`:
     - If `(nr, nc)` is an Empty Room (`INF`):
       - Update distance: `grid[nr][nc] = grid[r][c] + 1`.
       - Push to Queue.

**The Twist (Failure):** **The Infinite Overwrite.** If you update a cell that already has a distance, you might overwrite a shorter path with a longer one (if using DFS). BFS guarantees the first time you reach a room, it's via the shortest path.

**Interview Signal:** Identifying **Multi-Source BFS** use cases.

## 🚀 Approach & Intuition
Start BFS from all gates at once.

### C++ Pseudo-Code
```cpp
void wallsAndGates(vector<vector<int>>& rooms) {
    int m = rooms.size(), n = rooms[0].size();
    queue<pair<int, int>> q;
    
    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (rooms[r][c] == 0) q.push({r, c});
        }
    }
    
    int dirs[] = {0, 1, 0, -1, 0};
    while (!q.empty()) {
        auto [r, c] = q.front(); q.pop();
        for (int i = 0; i < 4; i++) {
            int nr = r + dirs[i], nc = c + dirs[i+1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && rooms[nr][nc] == INT_MAX) {
                rooms[nr][nc] = rooms[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }
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

- [Rotting Oranges](../rotting_oranges/PROBLEM.md) — Next in category
- [Clone Graph](../clone_graph/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
