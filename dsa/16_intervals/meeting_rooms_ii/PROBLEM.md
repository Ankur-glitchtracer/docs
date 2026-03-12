#  🏢 Intervals: Meeting Rooms II

## 📝 Description
[LeetCode 253](https://leetcode.com/problems/meeting-rooms-ii/) (Premium)
Given an array of meeting time intervals `intervals` where `intervals[i] = (To be detailed...)`, return the minimum number of conference rooms required.

## 🛠️ Requirements/Constraints

- $1 \le \text{intervals.length} \le 10^5$
- Intervals are given as $[start, end]$ pairs.

## 🧠 The Engineering Story

**The Villain:** "The Allocation Headache." We need to find the minimum number of conference rooms required. Merging intervals doesn't help (we need to run concurrent meetings, not combine them).

**The Hero:** "The Chronological Sweep (or Min-Heap)."

**The Plot:**

1. (To be detailed...)
2. (To be detailed...)

**The Twist (Failure):** **Heap Approach.** Keep a Min-Heap of *end times* of currently running meetings. `heap.size()` is the number of rooms needed.

**Interview Signal:** **Resource Allocation** logic.

## 🚀 Approach & Intuition
Count active overlaps.

### C++ Pseudo-Code
```cpp
int minMeetingRooms(vector<vector<int>>& intervals) {
    vector<int> starts, ends;
    for (auto& i : intervals) {
        starts.push_back(i[0]);
        ends.push_back(i[1]);
    }
    sort(starts.begin(), starts.end());
    sort(ends.begin(), ends.end());
    
    int res = 0, count = 0;
    int s = 0, e = 0;
    
    while (s < intervals.size()) {
        if (starts[s] < ends[e]) {
            s++;
            count++;
        } else {
            e++;
            count--;
        }
        res = max(res, count);
    }
    return res;
}
```

### Key Observations:

- Sorting intervals by their start or end time is almost always the first step in interval-based problems.
- Use a 'last end time' tracker or a Priority Queue to detect overlaps and manage active intervals.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$
    - **Space Complexity:** $O(N)$

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

- [Min Interval Each Query](../minimum_interval_to_include_each_query/PROBLEM.md) — Next in category
- [Meeting Rooms](../meeting_rooms/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
