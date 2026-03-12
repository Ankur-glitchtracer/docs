#  🏃 Greedy: Jump Game

## 📝 Description
[LeetCode 55](https://leetcode.com/problems/jump-game/)
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return `true` if you can reach the last index, or `false` otherwise.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Values represent jumps, costs, or intervals.

## 🧠 The Engineering Story

**The Villain:** "The Backtracker." Trying every jump combination ($O(2^N)$).

**The Hero:** "The Goal Shifter." Can we reach the end?

**The Plot:**

1. Maintain a `goal` index, initially the last index.
2. Iterate backwards from `n-2` to `0`.
3. If `i + nums[i] >= goal`: We can reach the goal from `i`.
   - Update `goal = i` (Now we just need to reach `i`).
4. If `goal == 0` at the end, return True.

**The Twist (Failure):** **Forward Greedy.** Maintaining `max_reach` going forward works too. If `i > max_reach`, return False. Both are $O(N)$.

**Interview Signal:** Simplifying **Reachability**.

## 🚀 Approach & Intuition
Move the goal post closer.

### C++ Pseudo-Code
```cpp
bool canJump(vector<int>& nums) {
    int goal = nums.size() - 1;
    for (int i = nums.size() - 1; i >= 0; i--) {
        if (i + nums[i] >= goal) goal = i;
    }
    return goal == 0;
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

- [Jump Game II](../jump_game_ii/PROBLEM.md) — Next in category
- [Maximum Subarray](../maximum_subarray/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
