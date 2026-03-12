#  🕒 Heap: Task Scheduler

## 📝 Description
[LeetCode 621](https://leetcode.com/problems/task-scheduler/)
Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle. However, there is a non-negative integer `n` that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks. Return the least number of units of times that the CPU will take to finish all the given tasks.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The Idle Time." We want to finish tasks as fast as possible, but identical tasks (e.g., 'A') need a cooldown `n`. Naively scheduling `A, B, A` might force a wait if `n` is large.

**The Hero:** "The Frequency Filler." The task with the highest frequency dictates the minimum length. We construct a "frame" based on the most frequent task.

**The Plot:**

1. Find the max frequency `max_f` (e.g., A appears 3 times).
2. We need `max_f - 1` groups of size `n + 1` (A followed by n slots).
3. The last group just has the remaining A's (and others with same max frequency).
4. Formula: `(max_f - 1) * (n + 1) + count_of_tasks_with_max_f`.
5. Result is `max(formula, total_tasks)` (we can never take less time than the number of tasks).

**The Twist (Failure):** **The Filling.** If we have enough other tasks to fill the empty slots, we don't need idles. The formula handles the idle case, the `max()` handles the "no idle" case.

**Interview Signal:** Mathematical modeling of **Scheduling Problems**.

## 🚀 Approach & Intuition
Calculate slots based on max frequency.

### C++ Pseudo-Code
```cpp
int leastInterval(vector<char>& tasks, int n) {
    vector<int> count(26, 0);
    int maxFreq = 0;
    for (char c : tasks) {
        count[c - 'A']++;
        maxFreq = max(maxFreq, count[c - 'A']);
    }
    
    int maxFreqCount = 0;
    for (int c : count) {
        if (c == maxFreq) maxFreqCount++;
    }
    
    int partCount = maxFreq - 1;
    int partLength = n - (maxFreqCount - 1);
    int emptySlots = partCount * partLength;
    int availableTasks = tasks.size() - (maxFreq * maxFreqCount);
    int idles = max(0, emptySlots - availableTasks);
    
    return tasks.size() + idles;
}
```

### Key Observations:

- Heaps are the go-to for finding the $K$-th largest or smallest element in $O(N \log K)$ time.
- Use a Min-Heap for $K$ largest elements and a Max-Heap for $K$ smallest elements to optimize space.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ (Counting)
    - **Space Complexity:** $O(1)$ (26 chars)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you implement a custom Heap from scratch? How would you implement a 'Decrease Key' operation?
- **Scale Question:** How would you maintain a Top-K list across 100 machines with frequent updates?
- **Edge Case Probe:** What if all elements have the same priority? How do you handle empty heap extractions?

## 🔗 Related Problems

- [Design Twitter](../design_twitter/PROBLEM.md) — Next in category
- [Kth Largest in Array](../kth_largest_element_in_an_array/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Maximum Subarray](../../15_greedy/maximum_subarray/PROBLEM.md) — Prerequisite for Greedy
