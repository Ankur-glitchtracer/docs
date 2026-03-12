#  ⭐ Greedy: Valid Parenthesis String

## 📝 Description
[LeetCode 678](https://leetcode.com/problems/valid-parenthesis-string/)
Given a string `s` containing only three types of characters: '(', ')' and '*', return `true` if `s` is valid. The '*' can be treated as a single right parenthesis ')', a single left parenthesis '(', or an empty string "".

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Values represent jumps, costs, or intervals.

## 🧠 The Engineering Story

**The Villain:** "The Backtracking Star." Treating `*` as `(`, `)`, or `` creates $3^N$ branches.

**The Hero:** "The Range Tracker." Instead of a single balance count, track the *possible range* of open parentheses `(To be detailed...)`.

**The Plot:**

1. `lo = 0, hi = 0`.
2. Iterate `c` in string:
   - `(` : `lo++`, `hi++`.
   - `)` : `lo--`, `hi--`.
   - `*` : `lo--` (treat as `)`), `hi++` (treat as `(`).
3. **Logic Check:**
   - If `hi < 0`: Too many closing parens. Impossible. Return False.
   - If `lo < 0`: `lo = 0`. (We can't have negative open parens, treat `*` as empty instead of `)`).
4. Return `lo == 0` (Can we satisfy the requirement of 0 open parens?).

**The Twist (Failure):** **Stack Approach.** You can use two stacks (indices of `(` and `*`), but the greedy range is $O(1)$ space.

**Interview Signal:** **Range Tracking** state.

## 🚀 Approach & Intuition
Track min and max possible open parentheses.

### C++ Pseudo-Code
```cpp
bool checkValidString(string s) {
    int lo = 0, hi = 0;
    for (char c : s) {
        if (c == '(') {
            lo++; hi++;
        } else if (c == ')') {
            lo--; hi--;
        } else {
            lo--; hi++;
        }
        if (hi < 0) return false;
        if (lo < 0) lo = 0;
    }
    return lo == 0;
}
```

### Key Observations:

- Greedy algorithms make the locally optimal choice at each step with the hope of finding a global optimum.
- The key is to prove that the greedy choice property and optimal substructure hold for the given problem.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$

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

- [Partition Labels](../partition_labels/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
