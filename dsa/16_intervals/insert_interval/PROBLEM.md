#  📥 Intervals: Insert Interval

## 📝 Description
[LeetCode 57](https://leetcode.com/problems/insert-interval/)
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = (To be detailed...)` represent the start and the end of the `i`th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval. Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary). Return `intervals` after the insertion.

## 🛠️ Requirements/Constraints

- $1 \le \text{intervals.length} \le 10^5$
- Intervals are given as $[start, end]$ pairs.

## 🧠 The Engineering Story

**The Villain:** "The Resorter." Adding the new interval and then sorting the whole list takes $O(N \log N)$.

**The Hero:** "The Linear Merge." The list is already sorted. We can find the correct spot and merge in $O(N)$.

**The Plot:**

1. **Left Part:** Add all intervals ending before `newInterval` starts.
2. **Merge Part:** While intervals overlap with `newInterval` (start <= newEnd), merge them:
   - `newStart = min(newStart, start)`
   - `newEnd = max(newEnd, end)`
3. Add the merged `newInterval`.
4. **Right Part:** Add remaining intervals.

**The Twist (Failure):** **Empty Inputs.** If intervals list is empty, just return `(To be detailed...)`.

**Interview Signal:** Exploiting **Sorted Inputs** for linear time operations.

## 🚀 Approach & Intuition
Add left, merge middle, add right.

### C++ Pseudo-Code
```cpp
vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    vector<vector<int>> res;
    int i = 0, n = intervals.size();
    
    // Left part (non-overlapping)
    while (i < n && intervals[i][1] < newInterval[0]) {
        res.push_back(intervals[i++]);
    }
    
    // Merging part
    while (i < n && intervals[i][0] <= newInterval[1]) {
        newInterval[0] = min(newInterval[0], intervals[i][0]);
        newInterval[1] = max(newInterval[1], intervals[i][1]);
        i++;
    }
    res.push_back(newInterval);
    
    // Right part
    while (i < n) {
        res.push_back(intervals[i++]);
    }
    
    return res;
}
```

### Key Observations:

- Sorting intervals by their start or end time is almost always the first step in interval-based problems.
- Use a 'last end time' tracker or a Priority Queue to detect overlaps and manage active intervals.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(N)$ (Result array)

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

- [Merge Intervals](../merge_intervals/PROBLEM.md) — Next in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
