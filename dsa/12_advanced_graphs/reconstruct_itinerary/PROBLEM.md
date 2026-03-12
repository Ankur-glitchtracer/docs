#  🗺️ Advanced Graph: Reconstruct Itinerary

## 📝 Description
[LeetCode 332](https://leetcode.com/problems/reconstruct-itinerary/)
You are given a list of airline `tickets` where `tickets[i] = (To be detailed...)` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it. The itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. You must use all the tickets once and only once.

## 🛠️ Requirements/Constraints

- $V \le 1000, E \le 10^4$
- Edge weights are non-negative for Dijkstra.

## 🧠 The Engineering Story

**The Villain:** "The Stuck Traveler." You need to use all plane tickets. Simply following the lexicographically smallest destination might get you stuck in a dead-end airport with tickets remaining elsewhere.

**The Hero:** "The Hierholzer's Algorithm (Eulerian Path)." An Eulerian Path visits every edge exactly once.

**The Plot:**

1. Build adjacency list: `from -> min_heap(to)` (sorted for lexicographical order).
2. Start DFS from "JFK".
3. **DFS Logic:**
   - While the current airport has destinations:
     - Pop the smallest destination.
     - Recurse into it.
   - After visiting all neighbors (stuck), add current airport to `result`.
4. The result is in reverse order. Reverse it to get the path.

**The Twist (Failure):** **Adding to path early.** If you add to path *before* recursion, you get stuck. You must add to path *after* visiting all edges (Post-Order), guaranteeing dead-ends are at the end of the list (which becomes the "end" of our journey).

**Interview Signal:** Mastery of **Eulerian Paths**.

## 🚀 Approach & Intuition
Visit edges until stuck, then add to path.

### C++ Pseudo-Code
```cpp
class Solution {
    unordered_map<string, priority_queue<string, vector<string>, greater<string>>> adj;
    vector<string> res;
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for (auto& t : tickets) adj[t[0]].push(t[1]);
        
        dfs("JFK");
        reverse(res.begin(), res.end());
        return res;
    }
    
    void dfs(string src) {
        while (!adj[src].empty()) {
            string dst = adj[src].top();
            adj[src].pop();
            dfs(dst);
        }
        res.push_back(src);
    }
};
```

### Key Observations:

- Dijkstra's and Prim's algorithms use a Priority Queue to find the shortest path or MST in $O(E \log V)$ time.
- Kruskal's algorithm uses Disjoint Set Union (DSU) to efficiently manage connected components and detect cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(E \log E)$ (Sorting edges)
    - **Space Complexity:** $O(E)$

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

- [Min Cost to Connect Points](../min_cost_to_connect_all_points/PROBLEM.md) — Next in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
