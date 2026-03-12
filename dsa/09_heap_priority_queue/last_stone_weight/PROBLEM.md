#  🪨 Heap: Last Stone Weight

## 📝 Description
[LeetCode 1046](https://leetcode.com/problems/last-stone-weight/)
You are given an array of integers `stones` where `stones[i]` is the weight of the `i`th stone. We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are destroyed, and
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`.
At the end of the game, there is at most one stone left. Return the weight of the last remaining stone. If there are no stones left, return `0`.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The Repeated Maximum." You constantly need the two heaviest stones to smash together. Linear scanning ($O(N)$) or re-sorting ($O(N \log N)$) every turn is too slow.

**The Hero:** "The Max-Heap." A structure designed to always give you the maximum element in $O(1)$ (access) or $O(\log N)$ (removal).

**The Plot:**

1. Put all stones into a Max-Heap.
2. While `size > 1`:
   - `y = pop()` (Heaviest).
   - `x = pop()` (Second heaviest).
   - If `x != y`, push `y - x`.
3. If heap is empty, return
0. Else, return `top()`.

**The Twist (Failure):** **The Zero Case.** If all stones smash completely, the heap is empty. The problem says return 0, not crash.

**Interview Signal:** Mastery of **Simulation with Priority Queues**.

## 🚀 Approach & Intuition
Simulate the process efficiently.

### C++ Pseudo-Code
```cpp
int lastStoneWeight(vector<int>& stones) {
    priority_queue<int> pq(stones.begin(), stones.end());
    while (pq.size() > 1) {
        int y = pq.top(); pq.pop();
        int x = pq.top(); pq.pop();
        if (x != y) pq.push(y - x);
    }
    return pq.empty() ? 0 : pq.top();
}
```

### Key Observations:

- Heaps are the go-to for finding the $K$-th largest or smallest element in $O(N \log K)$ time.
- Use a Min-Heap for $K$ largest elements and a Max-Heap for $K$ smallest elements to optimize space.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$ (Initial build + loops)
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

- [K Closest Points](../k_closest_points_to_origin/PROBLEM.md) — Next in category
- [Kth Largest in Stream](../kth_largest_element_in_a_stream/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Maximum Subarray](../../15_greedy/maximum_subarray/PROBLEM.md) — Prerequisite for Greedy
