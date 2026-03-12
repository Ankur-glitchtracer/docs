#  📦 Arrays & Hashing: Group Anagrams

## 📝 Description
[LeetCode 49](https://leetcode.com/problems/group-anagrams/)
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## 🛠️ Requirements/Constraints

- $1 \le strs.length \le 10^4$
- $0 \le strs[i].length \le 100$

## 🧠 The Engineering Story

**The Villain:** "The Pairwise Comparer." Comparing every string with every other string to check if they are anagrams ($O(N^2 \cdot K \log K)$).

**The Hero:** "The Canonical Key." Finding a representation where all anagrams look identical (e.g., sorting the string).

**The Plot:**

1. Initialize a Map where Key = Sorted String, Value = List of original strings.
2. Iterate through the input list.
3. Sort the current string to get the key (e.g., "eat" -> "aet").
4. Append the original string to the map entry for that key.
5. Return the values of the map.

**The Twist (Failure):** **The Sorting Bottleneck.** Sorting each string takes $O(K \log K)$. For very long strings, counting characters (e.g., "a1e1t1") is a faster key generation method ($O(K)$).

**Interview Signal:** Understanding of **Canonical Representations** and hashing.

## 🚀 Approach & Intuition
Sort each string to use as a hash map key.

### C++ Pseudo-Code
```cpp
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> mp;
    for (string s : strs) {
        string key = s;
        sort(key.begin(), key.end());
        mp[key].push_back(s);
    }
    vector<vector<string>> res;
    for (auto p : mp) res.push_back(p.second);
    return res;
}
```

### Key Observations:

- Sorting each string to use as a key in a hash map takes $O(N \cdot K \log K)$, where $K$ is the max length of a string.
- Using a character count tuple as a key reduces complexity to $O(N \cdot K)$.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \cdot K \log K)$ (Sorting) or $O(N \cdot K)$ (Counting)
    - **Space Complexity:** $O(N \cdot K)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you solve this without sorting the individual strings to generate keys? (e.g., using prime number products or character counts).
- **Scale Question:** How would you parallelize the grouping if the strings are stored across multiple machines in a distributed file system?
- **Edge Case Probe:** What if the input list contains very long strings (e.g., 1MB each) but only a few of them?

## 🔗 Related Problems

- [Top K Frequent Elements](../top_k_frequent_elements/PROBLEM.md) — Next in category
- [Two Sum](../two_sum/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
