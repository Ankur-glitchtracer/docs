#  🏃 Greedy: Jump Game II

## 📝 Description
[LeetCode 45](https://leetcode.com/problems/jump-game-ii/)
Given an array of non-negative integers `nums`, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You can assume that you can always reach the last index.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Values represent jumps, costs, or intervals.

## 🧠 The Engineering Story

**The Villain:** "The Shortest Path Search." BFS works ($O(N^2)$ edges in worst case). We need $O(N)$.

**The Hero:** "The BFS Optimization (Implicit Levels)." We don't need a queue. The range of nodes reachable at step `k` is `[l, r]`.

**The Plot:**

1. Current level range: `[l, r]`. Initially `[0, 0]`.
2. Find the `farthest` point reachable from any node in `[l, r]`.
3. Update range: `l = r + 1`, `r = farthest`.
4. Increment `jumps`.
5. Repeat until `r >= last_index`.

**The Twist (Failure):** **Unreachable.** The problem guarantees reachability. If not, check if `farthest <= r` (stuck).

**Interview Signal:** Optimizing **BFS into Greedy**.

## 🚀 Approach & Intuition
Level-by-level traversal without a queue.

### C++ Pseudo-Code
```cpp
int jump(vector<int>& nums) {
    int res = 0;
    int l = 0, r = 0;
    
    while (r < nums.size() - 1) {
        int farthest = 0;
        for (int i = l; i <= r; i++) {
            farthest = max(farthest, i + nums[i]);
        }
        l = r + 1;
        r = farthest;
        res++;
    }
    return res;
}
```

### Key Observations:

- Greedy algorithms make the locally optimal choice at each step with the hope of finding a global optimum.
- The key is to prove that the greedy choice property and optimal substructure hold for the given problem.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
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

- [Gas Station](../gas_station/PROBLEM.md) — Next in category
- [Jump Game](../jump_game/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
