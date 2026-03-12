#  ✂️ Greedy: Partition Labels

## 📝 Description
[LeetCode 763](https://leetcode.com/problems/partition-labels/)
You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`. Return a list of integers representing the size of these parts.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Values represent jumps, costs, or intervals.

## 🧠 The Engineering Story

**The Villain:** "The Recursive Cut." Trying to cut at every index and checking if it's valid.

**The Hero:** "The Last Occurrence Map."

**The Plot:**

1. **Pass 1:** Store the `last_index` of every char in a map/array.
2. **Pass 2:** Iterate `i` through string.
   - Update `end = max(end, last_index[s[i]])`.
   - If `i == end`: We reached the end of the current partition!
     - Add size to result.
     - Reset start anchor.

**The Twist (Failure):** **Overlapping Ranges.** 'a' ends at 5, 'b' is inside 'a's range but 'b' ends at 8. The `max()` ensures the partition extends to 8.

**Interview Signal:** **Interval Merging** logic on strings.

## 🚀 Approach & Intuition
Extend partition end to the last occurrence of current char.

### C++ Pseudo-Code
```cpp
vector<int> partitionLabels(string s) {
    unordered_map<char, int> lastIndex;
    for (int i = 0; i < s.length(); i++) lastIndex[s[i]] = i;
    
    vector<int> res;
    int size = 0, end = 0;
    
    for (int i = 0; i < s.length(); i++) {
        size++;
        end = max(end, lastIndex[s[i]]);
        
        if (i == end) {
            res.push_back(size);
            size = 0;
        }
    }
    return res;
}
```

### Key Observations:

- Greedy algorithms make the locally optimal choice at each step with the hope of finding a global optimum.
- The key is to prove that the greedy choice property and optimal substructure hold for the given problem.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (26 chars)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the input is sorted or has a limited range? Can you optimize space from $O(N)$ to $O(1)$?
- **Scale Question:** If the dataset is too large to fit in RAM, how would you use external sorting or a distributed hash table?
- **Edge Case Probe:** How does your solution handle duplicates, empty inputs, or extremely large integers?

## 🔗 Related Problems

- [Valid Parenthesis String](../valid_parenthesis_string/PROBLEM.md) — Next in category
- [Merge Triplets](../merge_triplets_to_form_target_triplet/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
