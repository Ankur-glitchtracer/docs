#  🔗 Intervals: Merge Intervals

## 📝 Description
[LeetCode 56](https://leetcode.com/problems/merge-intervals/)
Given an array of `intervals` where `intervals[i] = (To be detailed...)`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## 🛠️ Requirements/Constraints

- $1 \le \text{intervals.length} \le 10^5$
- Intervals are given as $[start, end]$ pairs.

## 🧠 The Engineering Story

**The Villain:** "The Unsorted Mess." If intervals aren't sorted, any interval could merge with any other. $O(N^2)$ checking.

**The Hero:** "The Sort & Sweep." Sort by start time. Now, overlapping intervals are adjacent.

**The Plot:**

1. Sort intervals by start time.
2. Initialize `result` with the first interval.
3. Iterate through the rest:
   - If `current_start <= last_merged_end`: **Overlap!**
     - `last_merged_end = max(last_merged_end, current_end)`.
   - Else: **No Overlap.**
     - Push current interval to `result`.

**The Twist (Failure):** **Lexicographical Sort.** `[1,4]` comes before `[1,3]`. Does it matter? No, because `end = max(4, 3) = 4` catches it regardless.

**Interview Signal:** The "Hello World" of **Interval Problems**.

## 🚀 Approach & Intuition
Sort by start, then merge adjacent if they overlap.

### C++ Pseudo-Code
```cpp
vector<vector<int>> merge(vector<vector<int>>& intervals) {
    if (intervals.empty()) return {};
    sort(intervals.begin(), intervals.end());
    
    vector<vector<int>> res;
    res.push_back(intervals[0]);
    
    for (int i = 1; i < intervals.size(); i++) {
        if (intervals[i][0] <= res.back()[1]) {
            res.back()[1] = max(res.back()[1], intervals[i][1]);
        } else {
            res.push_back(intervals[i]);
        }
    }
    return res;
}
```

### Key Observations:

- Sorting intervals by their start or end time is almost always the first step in interval-based problems.
- Use a 'last end time' tracker or a Priority Queue to detect overlaps and manage active intervals.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$ (Sorting)
    - **Space Complexity:** $O(N)$ (Result)

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

- [Non-overlapping Intervals](../non_overlapping_intervals/PROBLEM.md) — Next in category
- [Insert Interval](../insert_interval/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
