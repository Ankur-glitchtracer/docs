#  🎭 Graph: Clone Graph

## 📝 Description
[LeetCode 133](https://leetcode.com/problems/clone-graph/)
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph. Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Infinite Loop." A graph can have cycles ($A \to B \to A$). If you just recursively copy neighbors, you'll enter an infinite loop creating infinite copies of A and B.

**The Hero:** "The HashMap Cache." We need to remember which nodes we've already copied. `OldNode -> NewNode`.

**The Plot:**

1. Use a HashMap `visited`.
2. **DFS(node):**
   - If `node` in `visited`: Return `visited[node]`.
   - Create `newNode` with `node.val`.
   - Add to `visited` **immediately** (before recursing).
   - For each neighbor of `node`:
     - `newNode.neighbors.add(DFS(neighbor))`.
   - Return `newNode`.

**The Twist (Failure):** **Adding after recursion.** If you add to the map *after* the recursive calls, the cycle check will fail because the node isn't "registered" yet when the child tries to point back to it.

**Interview Signal:** Handling **Cycles** and deep copying complex structures.

## 🚀 Approach & Intuition
Map original nodes to clones to handle cycles.

### C++ Pseudo-Code
```cpp
class Solution {
    unordered_map<Node*, Node*> visited;
public:
    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;
        if (visited.count(node)) return visited[node];
        
        Node* clone = new Node(node->val);
        visited[node] = clone;
        
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(cloneGraph(neighbor));
        }
        return clone;
    }
};
```

### Key Observations:

- Represent the graph using an Adjacency List for space efficiency in sparse graphs.
- Use DFS for path-finding/connectivity and BFS for finding the shortest path in unweighted graphs.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(V + E)$
    - **Space Complexity:** $O(V)$

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

- [Walls and Gates](../walls_and_gates/PROBLEM.md) — Next in category
- [Max Area of Island](../max_area_of_island/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
