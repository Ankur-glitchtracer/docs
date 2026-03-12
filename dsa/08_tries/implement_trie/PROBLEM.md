#  🌳 Trie: Implement Trie (Prefix Tree)

## 📝 Description
[LeetCode 208](https://leetcode.com/problems/implement-trie-prefix-tree/)
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker. Implement the Trie class.

## 🛠️ Requirements/Constraints

- $1 \le \text{word.length} \le 2000$
- Words consist of lowercase English letters.

## 🧠 The Engineering Story

**The Villain:** "The Prefix Scan." You have 1 million strings. To check if any string starts with "app", you have to scan all 1 million strings ($O(N \cdot L)$).

**The Hero:** "The Tree of Characters." A tree where each node represents a character. "apple" is stored as `root -> a -> p -> p -> l -> e`.

**The Plot:**

1. **Node Structure:** Array of 26 pointers (children) and a boolean `isEnd`.
2. **Insert:** Traverse down from root. Create new nodes if child pointer is null. Mark the last node's `isEnd = true`.
3. **Search:** Traverse down. If any child pointer is null, return `false`. At the end, return `node.isEnd`.
4. **StartsWith:** Same as Search, but return `true` even if `node.isEnd` is false.

**The Twist (Failure):** **Memory Usage.** A Trie consumes a lot of memory because of the arrays of pointers. In production, we might use a Hash Map for children to save space (sparse nodes).

**Interview Signal:** Implementation of **Tree-based Dictionaries**.

## 🚀 Approach & Intuition
Standard Trie implementation.

### C++ Pseudo-Code
```cpp
class Trie {
    struct Node {
        Node* children[26] = {nullptr};
        bool isEnd = false;
    };
    Node* root;
public:
    Trie() { root = new Node(); }
    
    void insert(string word) {
        Node* curr = root;
        for (char c : word) {
            if (!curr->children[c - 'a'])
                curr->children[c - 'a'] = new Node();
            curr = curr->children[c - 'a'];
        }
        curr->isEnd = true;
    }
    
    bool search(string word) {
        Node* curr = root;
        for (char c : word) {
            if (!curr->children[c - 'a']) return false;
            curr = curr->children[c - 'a'];
        }
        return curr->isEnd;
    }
    
    bool startsWith(string prefix) {
        Node* curr = root;
        for (char c : prefix) {
            if (!curr->children[c - 'a']) return false;
            curr = curr->children[c - 'a'];
        }
        return true;
    }
};
```

### Key Observations:

- Tries are ideal for prefix-based searches and autocomplete features, providing $O(L)$ time for words of length $L$.
- Each node typically contains a hash map or array of size 26 for its children, plus a boolean flag for the end of a word.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(L)$ for Insert, Search, StartsWith.
    - **Space Complexity:** $O(N \cdot L)$ total characters stored.

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

- [Add and Search Words](../design_add_and_search_words_data_structure/PROBLEM.md) — Next in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite: Trees
