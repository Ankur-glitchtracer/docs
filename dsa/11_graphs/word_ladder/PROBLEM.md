#  🪜 Graph: Word Ladder

## 📝 Description
[LeetCode 127](https://leetcode.com/problems/word-ladder/)
A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that every adjacent pair differs by a single letter, and every `si` is in `wordList`. Return the number of words in the shortest transformation sequence, or 0 if no such sequence exists.

## 🛠️ Requirements/Constraints

- $V, E \le 10^5$ (Nodes and Edges)
- The graph can be directed or undirected.

## 🧠 The Engineering Story

**The Villain:** "The Transformation Maze." Getting from "hit" to "cog" by changing one letter at a time ("hot", "dot", "dog"...). This is a shortest path problem on an unweighted graph.

**The Hero:** "The BFS Transformation."

**The Plot:**

1. **Nodes:** Words.
2. **Edges:** Words differing by exactly 1 char.
3. **Algorithm:** BFS (Queue) for shortest path.
4. **Optimization:** Instead of iterating all 5000 words to find neighbors ($O(N \cdot L)$), iterate the 26 possible chars for each position ($O(26 \cdot L)$).
   - "hot" -> "_ot", "h_t", "ho_" -> Check if these variants exist in the dictionary.

**The Twist (Failure):** **Dictionary Lookup.** If you use a List for the dictionary, lookups are $O(N)$. Convert to a Hash Set for $O(1)$ lookups.

**Interview Signal:** Modeling **String Transformation as a Graph**.

## 🚀 Approach & Intuition
Breadth-first search for shortest path.

### C++ Pseudo-Code
```cpp
int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
    unordered_set<string> dict(wordList.begin(), wordList.end());
    if (!dict.count(endWord)) return 0;
    
    queue<string> q;
    q.push(beginWord);
    int step = 1;
    
    while (!q.empty()) {
        int sz = q.size();
        while (sz--) {
            string word = q.front(); q.pop();
            if (word == endWord) return step;
            
            for (int i = 0; i < word.size(); i++) {
                char original = word[i];
                for (char c = 'a'; c <= 'z'; c++) {
                    word[i] = c;
                    if (dict.count(word)) {
                        dict.erase(word); // Mark visited
                        q.push(word);
                    }
                }
                word[i] = original; // Restore
            }
        }
        step++;
    }
    return 0;
}
```

### Key Observations:

- Represent the graph using an Adjacency List for space efficiency in sparse graphs.
- Use DFS for path-finding/connectivity and BFS for finding the shortest path in unweighted graphs.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M^2 \cdot N)$ where M is word length, N is list size.
    - **Space Complexity:** $O(M \cdot N)$

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

- [Redundant Connection](../redundant_connection/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Rotate Image](../../17_math_geometry/rotate_image/PROBLEM.md) — Prerequisite for Math & Geometry
