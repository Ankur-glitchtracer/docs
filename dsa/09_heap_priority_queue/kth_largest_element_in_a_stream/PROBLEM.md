#  📊 Heap: Kth Largest Element in a Stream

## 📝 Description
[LeetCode 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
Design a class to find the `k`th largest element in a stream. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The Infinite Sorter." You have a continuous stream of numbers. If you sort the entire list every time a new number arrives ($O(N \log N)$), your system will crawl to a halt.

**The Hero:** "The Gatekeeper Min-Heap." We only care about the *top k* largest elements. The smallest of these "top k" is our answer.

**The Plot:**

1. Maintain a Min-Heap of size `k`.
2. When adding a number:
   - Push to heap.
   - If heap size > k, pop the smallest element.
3. The top of the heap is always the $k^{th}$ largest seen so far.

**The Twist (Failure):** **The Max-Heap Trap.** A Max-Heap keeps the largest element at the top. We want the $k^{th}$ largest, which is the *smallest* of the big guys.

**Interview Signal:** Efficiently processing **Streaming Data**.

## 🚀 Approach & Intuition
Keep only the K largest elements. The smallest of them is the Kth largest.

### C++ Pseudo-Code
```cpp
class KthLargest {
    priority_queue<int, vector<int>, greater<int>> pq;
    int k;
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int x : nums) add(x);
    }
    
    int add(int val) {
        pq.push(val);
        if (pq.size() > k) pq.pop();
        return pq.top();
    }
};
```

### Key Observations:

- Heaps are the go-to for finding the $K$-th largest or smallest element in $O(N \log K)$ time.
- Use a Min-Heap for $K$ largest elements and a Max-Heap for $K$ smallest elements to optimize space.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log k)$ per add.
    - **Space Complexity:** $O(k)$

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

- [Last Stone Weight](../last_stone_weight/PROBLEM.md) — Next in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Maximum Subarray](../../15_greedy/maximum_subarray/PROBLEM.md) — Prerequisite for Greedy
- [Insert Interval](../../16_intervals/insert_interval/PROBLEM.md) — Prerequisite for Intervals
