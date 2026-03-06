# 🌳 Topic Overview: Trees & Graphs

Mastering non-linear data structures involves understanding traversal (DFS/BFS) and shortest path algorithms.

## 🔑 Key Concepts Checklist
- [ ] **BFS (Breadth-First Search):** Using a `queue`. Best for shortest path in unweighted graphs or level-order traversal.
- [ ] **DFS (Depth-First Search):** Using recursion or a `stack`. Best for exploring all paths or finding connectivity.
- [ ] **Union-Find (Disjoint Set):** Cycle detection in undirected graphs, Kruskal's algorithm.
- [ ] **Topological Sort (Kahn's Algorithm):** Dependency resolution (e.g., Course Schedule).
- [ ] **Dijkstra's Algorithm:** Shortest path in weighted graphs (no negative weights) using a `priority_queue`.
- [ ] **Trie (Prefix Tree):** Efficient string search and prefix matching.

## 🎯 Essential Problem Checklist (95% Coverage)
| Problem | Key Concept | Difficulty |
| :--- | :--- | :--- |
| **Level Order Traversal** | BFS (Queue) | Medium |
| **Max Depth of Binary Tree** | DFS (Recursion) | Easy |
| **Validate BST** | DFS (Range validation) | Medium |
| **LCA of Binary Tree** | DFS (Path finding) | Medium |
| **Number of Islands** | DFS/BFS (Grid) | Medium |
| **Clone Graph** | DFS/BFS (HashMap mapping) | Medium |
| **Course Schedule** | Topological Sort | Medium |
| **Network Delay Time** | Dijkstra | Medium |
| **Word Ladder** | BFS (Shortest Path) | Hard |
| **Alien Dictionary** | Topological Sort | Hard |

## ⏱️ Complexity Cheatsheet
| Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| DFS / BFS (Tree) | $O(N)$ | $O(H)$ (Height) or $O(W)$ (Width) |
| DFS / BFS (Graph) | $O(V + E)$ | $O(V)$ |
| Dijkstra | $O(E \log V)$ | $O(V + E)$ |
| Topological Sort | $O(V + E)$ | $O(V)$ |

## 📚 Recommended Reading (CP-Algorithms)
- [Breadth-First Search (BFS)](https://cp-algorithms.com/graph/breadth-first-search.html)
- [Depth-First Search (DFS)](https://cp-algorithms.com/graph/depth-first-search.html)
- [Dijkstra's Algorithm (Shortest Paths)](https://cp-algorithms.com/graph/dijkstra.html)
- [Disjoint Set Union (DSU/Union-Find)](https://cp-algorithms.com/data_structures/disjoint_set_union.html)
- [Topological Sort (Kahn's & DFS)](https://cp-algorithms.com/graph/topological-sort.html)
- [Lowest Common Ancestor (LCA)](https://cp-algorithms.com/graph/lca.html)
- [Trie (Prefix Tree) Implementation](https://cp-algorithms.com/string/aho_corasick.html#aho-corasick-algorithm)

## 🔗 External References
- [Graph Traversal Visualizations (VisuAlgo)](https://visualgo.net/en/dfsbfs)
- [Introduction to Trees (Khan Academy)](https://www.khanacademy.org/computing/computer-science/algorithms)
