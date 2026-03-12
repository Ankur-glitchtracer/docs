#  ⏱️ Binary Search: Time Based Key-Value Store

## 📝 Description
[LeetCode 981](https://leetcode.com/problems/time-based-key-value-store/)
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Target value is within the range of the data type.

## 🧠 The Engineering Story

**The Villain:** "The Linear History Search." Storing history as a list `(To be detailed...)` and scanning it linearly to find the right timestamp ($O(N)$). Slow for keys with huge history.

**The Hero:** "The Timestamp Indexer." Store history in a map: `Key -> List(To be detailed...)`. Since timestamps are strictly increasing, the list is sorted!

**The Plot:**

1. `set(key, value, timestamp)`: Append to the list for `key`.
2. `get(key, timestamp)`: Use **Binary Search** (specifically `upper_bound` or equivalent) on the list to find the largest timestamp `<= query_time`.
3. If found, return value. Else, return empty string.

**The Twist (Failure):** **The Exact Match Trap.** We want the closest timestamp *less than or equal to* the query. Standard binary search finds exact matches. You need logic for "floor" or "predecessor."

**Interview Signal:** Designing **Data Structures** on top of algorithms.

## 🚀 Approach & Intuition
Map key to a sorted list of pairs. Search the list.

### C++ Pseudo-Code
```cpp
class TimeMap {
    unordered_map<string, vector<pair<int, string>>> m;
public:
    void set(string key, string value, int timestamp) {
        m[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        if (!m.count(key)) return "";
        auto& v = m[key];
        
        // Binary search for timestamp <= target
        int l = 0, r = v.size() - 1;
        string res = "";
        
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (v[mid].first <= timestamp) {
                res = v[mid].second;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }
};
```

### Key Observations:

- Binary search can be applied not just to sorted arrays, but to any monotonic search space (Search on Answer).
- Be careful with the boundaries ($left, right$) and the condition for moving them to avoid infinite loops.

!!! info "Complexity Analysis"

    - **Time Complexity:** `set`: $O(1)$ (Append), `get`: $O(\log N)$ (Binary Search)
    - **Space Complexity:** $O(N)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you apply 'Binary Search on Answer' to solve optimization problems (e.g., minimize max distance)?
- **Scale Question:** If you are searching in a distributed database, how can you reduce the number of network round trips?
- **Edge Case Probe:** Does your mid-point calculation `(left + right) / 2` overflow for very large indices?

## 🔗 Related Problems

- [Median of Two Sorted Arrays](../median_of_two_sorted_arrays/PROBLEM.md) — Next in category
- [Search in Rotated Array](../search_in_rotated_sorted_array/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
