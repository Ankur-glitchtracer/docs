#  🚫 Intervals: Non-overlapping Intervals

## 📝 Description
[LeetCode 435](https://leetcode.com/problems/non-overlapping-intervals/)
Given an array of intervals `intervals` where `intervals[i] = (To be detailed...)`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

## 🛠️ Requirements/Constraints

- $1 \le \text{intervals.length} \le 10^5$
- Intervals are given as $[start, end]$ pairs.

## 🧠 The Engineering Story

**The Villain:** "The Greedy Confusion." Do I keep the interval that starts earliest? Or the longest one?

**The Hero:** "The Early Finisher." Keep the interval that ends *earliest*. Why? Because ending early leaves more room for future intervals.

**The Plot:**

1. Sort by **End Time**.
2. `end_limit = -inf`, `count = 0` (count non-overlapping).
3. Iterate intervals:
   - If `start >= end_limit`: No overlap.
     - `count++`
     - `end_limit = end`.
   - Else: Overlap. Skip it (implicitly removed).
4. Result = `Total - count`.

**The Twist (Failure):** **Sorting by Start Time.** It works too, but logic is slightly different: if overlap, discard the one with the *later* end time (keep the one that finishes first).

**Interview Signal:** **Greedy Selection Criteria** (Activity Selection Problem).

## 🚀 Approach & Intuition
Select intervals that finish earliest to maximize capacity.

### C++ Pseudo-Code
```cpp
int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
        return a[1] < b[1];
    });
    
    int count = 0;
    int end = INT_MIN;
    for (const auto& i : intervals) {
        if (i[0] >= end) {
            end = i[1];
        } else {
            count++;
        }
    }
    return count;
}
```

### Key Observations:

- Sorting intervals by their start or end time is almost always the first step in interval-based problems.
- Use a 'last end time' tracker or a Priority Queue to detect overlaps and manage active intervals.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$
    - **Space Complexity:** $O(1)$ (ignoring sort stack)

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

- [Meeting Rooms](../meeting_rooms/PROBLEM.md) — Next in category
- [Merge Intervals](../merge_intervals/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
