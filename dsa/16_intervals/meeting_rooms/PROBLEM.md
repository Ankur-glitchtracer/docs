#  🤝 Intervals: Meeting Rooms

## 📝 Description
[LeetCode 252](https://leetcode.com/problems/meeting-rooms/) (Premium)
Given an array of meeting time intervals where `intervals[i] = (To be detailed...)`, determine if a person could attend all meetings.

## 🛠️ Requirements/Constraints

- $1 \le \text{intervals.length} \le 10^5$
- Intervals are given as $[start, end]$ pairs.

## 🧠 The Engineering Story

**The Villain:** "The Double Booking." Can a person attend all meetings? Not if any two overlap.

**The Hero:** "The Overlap Check." Just sort and check adjacent pairs.

**The Plot:**

1. Sort intervals by start time.
2. Iterate from 0 to `n-2`.
3. If `intervals[i].end > intervals[i+1].start`: Overlap detected! Return `false`.
4. If loop finishes, return `true`.

**The Twist (Failure):** **Edge touching.** Usually `[1, 2]` and `[2, 3]` are NOT overlapping. Use `>` strictly, not `>=`.

**Interview Signal:** Basic **Interval Sorting**.

## 🚀 Approach & Intuition
Verify if any `end[i] > start[i+1]`.

### C++ Pseudo-Code
```cpp
bool canAttendMeetings(vector<vector<int>>& intervals) {
    sort(intervals.begin(), intervals.end());
    for (int i = 0; i < (int)intervals.size() - 1; i++) {
        if (intervals[i][1] > intervals[i+1][0]) return false;
    }
    return true;
}
```

### Key Observations:

- Sorting intervals by their start or end time is almost always the first step in interval-based problems.
- Use a 'last end time' tracker or a Priority Queue to detect overlaps and manage active intervals.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$
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

- [Meeting Rooms II](../meeting_rooms_ii/PROBLEM.md) — Next in category
- [Non-overlapping Intervals](../non_overlapping_intervals/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
