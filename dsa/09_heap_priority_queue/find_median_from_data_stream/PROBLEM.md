#  ⚖️ Heap: Find Median from Data Stream

## 📝 Description
[LeetCode 295](https://leetcode.com/problems/find-median-from-data-stream/)
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values. Design a data structure that supports adding integers and finding the median.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The Dynamic Sorter." Keeping a list sorted as numbers arrive ($O(N)$ insertion) makes getting the median fast ($O(1)$) but insertion slow. Or, sorting on demand makes retrieval slow ($O(N \log N)$).

**The Hero:** "The Two-Heap Balance." We split the data into two halves: Small Half and Large Half.

**The Plot:**

1. **Max-Heap (`small`):** Stores the smaller half of numbers. Top is the largest of the smalls (middle-left).
2. **Min-Heap (`large`):** Stores the larger half. Top is the smallest of the bigs (middle-right).
3. **Balancing Act:** Ensure `size(small) == size(large)` or `size(small) == size(large) + 1`.
4. **Median:**
   - If sizes equal: `(small.top + large.top) / 2`.
   - If odd: `small.top`.

**The Twist (Failure):** **The Cross-Over.** You can't just push to one heap blindly. You must push to one, pop its top, and push that to the other to ensure the order is maintained.

**Interview Signal:** Managing **Data Structure Invariants**.

## 🚀 Approach & Intuition
Maintain two halves of the data.

### C++ Pseudo-Code
```cpp
class MedianFinder {
    priority_queue<int> small; // Max heap
    priority_queue<int, vector<int>, greater<int>> large; // Min heap
public:
    void addNum(int num) {
        small.push(num);
        large.push(small.top());
        small.pop();
        
        if (small.size() < large.size()) {
            small.push(large.top());
            large.pop();
        }
    }
    
    double findMedian() {
        if (small.size() > large.size()) return small.top();
        return (small.top() + large.top()) / 2.0;
    }
};
```

### Key Observations:

- Heaps are the go-to for finding the $K$-th largest or smallest element in $O(N \log K)$ time.
- Use a Min-Heap for $K$ largest elements and a Max-Heap for $K$ smallest elements to optimize space.

!!! info "Complexity Analysis"

    - **Time Complexity:** Add: $O(\log N)$, Find: $O(1)$.
    - **Space Complexity:** $O(N)$

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

- [Design Twitter](../design_twitter/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Maximum Subarray](../../15_greedy/maximum_subarray/PROBLEM.md) — Prerequisite for Greedy
- [Insert Interval](../../16_intervals/insert_interval/PROBLEM.md) — Prerequisite for Intervals
