#  🔎 Trie: Word Search II

## 📝 Description
[LeetCode 212](https://leetcode.com/problems/word-search-ii/)
Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## 🛠️ Requirements/Constraints

- $1 \le \text{word.length} \le 2000$
- Words consist of lowercase English letters.

## 🧠 The Engineering Story

**The Villain:** "The Repeated Scan." Calling `exist(board, word)` for every single word in the dictionary. If you have 1000 words, you scan the board 1000 times.

**The Hero:** "The Inverted Search." Put all words into a Trie. Scan the board *once*. As you traverse the grid (DFS), simultaneously traverse the Trie.

**The Plot:**

1. Build a Trie from `words`.
2. Iterate every cell `(r, c)`. Start DFS if `board[r][c]` is a child of Trie Root.
3. **DFS(r, c, trieNode):**
   - If `trieNode.word` is set: We found a word! Add to results. (Optimization: Remove word from Trie to avoid duplicates).
   - Mark `board[r][c]` visited.
   - For each neighbor, check if `neighbor_char` exists in `trieNode.children`.
   - Recurse: `dfs(nr, nc, trieNode.children(To be detailed...))`.
   - Backtrack.

**The Twist (Failure):** **Duplicate Results.** The same word might be found multiple times on the board. Store results in a Set or remove the word from the Trie (set `isEnd = false`) immediately after finding it.

**Interview Signal:** Advanced **Optimization** by combining Data Structures.

## 🚀 Approach & Intuition
DFS on board guided by Trie nodes.

### C++ Pseudo-Code
```cpp
class Solution {
    struct Node {
        Node* children[26] = {nullptr};
        string* word = nullptr; // Store pointer to word at end node
    };
    Node* root = new Node();
    
    void insert(string& s) {
        Node* curr = root;
        for (char c : s) {
            if (!curr->children[c - 'a']) curr->children[c - 'a'] = new Node();
            curr = curr->children[c - 'a'];
        }
        curr->word = &s;
    }
    
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        for (string& w : words) insert(w);
        vector<string> res;
        int m = board.size(), n = board[0].size();
        
        function<void(int, int, Node*)> dfs = [&](int r, int c, Node* node) {
            char ch = board[r][c];
            if (ch == '#' || !node->children[ch - 'a']) return;
            
            node = node->children[ch - 'a'];
            if (node->word) {
                res.push_back(*node->word);
                node->word = nullptr; // Avoid duplicates
            }
            
            board[r][c] = '#';
            int dirs[] = {0, 1, 0, -1, 0};
            for (int i = 0; i < 4; i++) {
                int nr = r + dirs[i], nc = c + dirs[i+1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n)
                    dfs(nr, nc, node);
            }
            board[r][c] = ch;
        };
        
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                dfs(r, c, root);
                
        return res;
    }
};
```

### Key Observations:

- Tries are ideal for prefix-based searches and autocomplete features, providing $O(L)$ time for words of length $L$.
- Each node typically contains a hash map or array of size 26 for its children, plus a boolean flag for the end of a word.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(M \cdot N \cdot 4^L)$ theoretically, but Trie pruning makes it much faster.
    - **Space Complexity:** $O(TotalChars)$.

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** How would you solve this iteratively if you were worried about stack overflow from deep recursion?
- **Scale Question:** If the tree is a multi-terabyte B-Tree in a database, how do you optimize node traversal to minimize disk hits?
- **Edge Case Probe:** What if the tree is extremely skewed (effectively a linked list)? What if it's empty?

## 🔗 Related Problems

- [Add and Search Words](../design_add_and_search_words_data_structure/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite: Trees
