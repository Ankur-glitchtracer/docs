#  👽 Advanced Graph: Alien Dictionary

## 📝 Description
[LeetCode 269](https://leetcode.com/problems/alien-dictionary/)
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you. You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are sorted lexicographically by the rules of this new language. Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

## 🛠️ Requirements/Constraints

- $V \le 1000, E \le 10^4$
- Edge weights are non-negative for Dijkstra.

## 🧠 The Engineering Story

**The Villain:** "The Unknown Alphabet." You have a list of words sorted lexicographically in an alien language. You need to derive the alphabet order.

**The Hero:** "The Dependency Graph." If "wrt" comes before "wrf", then 't' must come before 'f'.

**The Plot:**

1. **Build Graph:**
   - Compare adjacent words (`words[i]` and `words[i+1]`).
   - Find the first differing character: `c1 != c2`.
   - Add edge `c1 -> c2`.
2. **Topological Sort:**
   - Compute indegrees.
   - Run Kahn's Algorithm (BFS).
3. **Validation:**
   - If cycle detected (output length < unique chars), return "".
   - Special case: "abc" before "ab" is invalid (prefix rule).

**The Twist (Failure):** **The Prefix Bug.** If `words = (To be detailed...)`, the input is invalid because "app" is a prefix of "apple" but comes later. Standard graph logic won't catch this without an explicit check.

**Interview Signal:** **Topological Sort** from derived constraints.

## 🚀 Approach & Intuition
Build adjacency list from adjacent word differences.

### C++ Pseudo-Code
```cpp
string alienOrder(vector<string>& words) {
    unordered_map<char, unordered_set<char>> adj;
    unordered_map<char, int> indegree;
    for (string s : words) for (char c : s) indegree[c] = 0;
    
    for (int i = 0; i < words.size() - 1; i++) {
        string w1 = words[i], w2 = words[i+1];
        if (w1.size() > w2.size() && w1.substr(0, w2.size()) == w2) return "";
        for (int j = 0; j < min(w1.size(), w2.size()); j++) {
            if (w1[j] != w2[j]) {
                if (!adj[w1[j]].count(w2[j])) {
                    adj[w1[j]].insert(w2[j]);
                    indegree[w2[j]]++;
                }
                break;
            }
        }
    }
    
    queue<char> q;
    for (auto& p : indegree) if (p.second == 0) q.push(p.first);
    
    string res = "";
    while (!q.empty()) {
        char u = q.front(); q.pop();
        res += u;
        for (char v : adj[u]) {
            if (--indegree[v] == 0) q.push(v);
        }
    }
    return res.size() == indegree.size() ? res : "";
}
```

### Key Observations:

- Dijkstra's and Prim's algorithms use a Priority Queue to find the shortest path or MST in $O(E \log V)$ time.
- Kruskal's algorithm uses Disjoint Set Union (DSU) to efficiently manage connected components and detect cycles.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(C)$ (Total characters)
    - **Space Complexity:** $O(1)$ (26 chars)

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

- [Cheapest Flights K Stops](../cheapest_flights_within_k_stops/PROBLEM.md) — Next in category
- [Swim in Rising Water](../swim_in_rising_water/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
- [Number of Islands](../../11_graphs/number_of_islands/PROBLEM.md) — Prerequisite: Graphs
