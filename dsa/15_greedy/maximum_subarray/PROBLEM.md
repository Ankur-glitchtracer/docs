#  💰 Greedy: Maximum Subarray

## 📝 Description
[LeetCode 53](https://leetcode.com/problems/maximum-subarray/)
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Values represent jumps, costs, or intervals.

## 🧠 The Engineering Story

**The Villain:** "The O(N^2) Scan." Checking every possible subarray.

**The Hero:** "Kadane's Algorithm." The logic: "If my current running sum is negative, it's garbage. Throw it away and start fresh."

**The Plot:**

1. Initialize `maxSub` and `curSum`.
2. Iterate through numbers.
3. If `curSum < 0`, reset `curSum = 0`.
4. `curSum += n`.
5. `maxSub = max(maxSub, curSum)`.

**The Twist (Failure):** **All Negatives.** If array is `[-2, -1]`, resetting `curSum` to 0 might return 0, which is wrong. The result should be -1. Initialize `maxSub` to `nums[0]`, not 0.

**Interview Signal:** The standard for **Linear Time Subarray** problems.

## 🚀 Approach & Intuition
Discard negative prefixes.

### C++ Pseudo-Code
```cpp
int maxSubArray(vector<int>& nums) {
    int maxSub = nums[0];
    int curSum = 0;
    
    for (int n : nums) {
        if (curSum < 0) curSum = 0;
        curSum += n;
        maxSub = max(maxSub, curSum);
    }
    return maxSub;
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

- [Jump Game](../jump_game/PROBLEM.md) — Next in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
