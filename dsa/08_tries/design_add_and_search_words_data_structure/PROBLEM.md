#  🌳 Trie: Design Add and Search Words Data Structure

## 📝 Description
[LeetCode 211](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
Design a data structure that supports adding new words and finding if a string matches any previously added string. The search string may contain dots '.' where a dot can be matched with any letter.

## 🛠️ Requirements/Constraints

- $1 \le \text{word.length} \le 2000$
- Words consist of lowercase English letters.

## 🧠 The Engineering Story

**The Villain:** "The Wildcard." Standard Tries handle exact matches. But how do you handle "b.d" where `.` can be any letter?

**The Hero:** "The DFS Search." When we hit a `.`, we can't take just one path. We must try *all* possible children of the current node.

**The Plot:**

1. **AddWord:** Standard Trie insert.
2. **Search:** Recursive DFS function `search(index, node)`.
3. If `word[index]` is a letter: Go to `node->children[letter]`. If null, return False.
4. If `word[index]` is `.`: Loop through all 26 children. If *any* recursive call returns True, then True.

**The Twist (Failure):** **The Base Case.** Don't forget `isEnd`. Just reaching the end of the string isn't enough; the current node must mark the end of a valid word.

**Interview Signal:** Adapting Data Structures for **Fuzzy Matching**.

## 🚀 Approach & Intuition
Handle '.' by exploring all branches.

### C++ Pseudo-Code
```cpp
class WordDictionary {
    struct Node {
        Node* children[26] = {nullptr};
        bool isEnd = false;
    };
    Node* root;
public:
    WordDictionary() { root = new Node(); }
    
    void addWord(string word) {
        Node* curr = root;
        for (char c : word) {
            if (!curr->children[c - 'a'])
                curr->children[c - 'a'] = new Node();
            curr = curr->children[c - 'a'];
        }
        curr->isEnd = true;
    }
    
    bool search(string word) {
        return dfs(word, 0, root);
    }
    
    bool dfs(string& word, int i, Node* curr) {
        if (!curr) return false;
        if (i == word.size()) return curr->isEnd;
        
        if (word[i] != '.') {
            return dfs(word, i + 1, curr->children[word[i] - 'a']);
        } else {
            for (int j = 0; j < 26; j++) {
                if (dfs(word, i + 1, curr->children[j])) return true;
            }
            return false;
        }
    }
};
```

### Key Observations:

- Tries are ideal for prefix-based searches and autocomplete features, providing $O(L)$ time for words of length $L$.
- Each node typically contains a hash map or array of size 26 for its children, plus a boolean flag for the end of a word.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(L)$ for Add. $O(26^L)$ worst case for Search with dots (basically DFS).
    - **Space Complexity:** $O(N \cdot L)$.

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

- [Word Search II](../word_search_ii/PROBLEM.md) — Next in category
- [Implement Trie](../implement_trie/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite: Trees
