#  ⛽ Greedy: Gas Station

## 📝 Description
[LeetCode 134](https://leetcode.com/problems/gas-station/)
There are `n` gas stations along a circular route, where the amount of gas at the `i`th station is `gas[i]`. You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i`th station to its next `(i + 1)`th station. You begin the journey with an empty tank at one of the gas stations. Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is guaranteed to be unique.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Values represent jumps, costs, or intervals.

## 🧠 The Engineering Story

**The Villain:** "The Simulation Loop." Trying to start at index 0, then 1, then 2... ($O(N^2)$).

**The Hero:** "The Total Tank Check."

**The Plot:**

1. Iterate `i` from 0 to `n`.
2. `total += gas[i] - cost[i]`.
3. If `total < 0`:
   - We failed to reach `i` from `start`.
   - Any station between `start` and `i` also fails.
   - Set `start = i + 1` and `total = 0`.

**The Twist (Failure):** **Why unique?** If sum(gas) >= sum(cost), a solution is guaranteed. We find the *first* valid one.

**Interview Signal:** Using **Global Properties** to simplify search.

## 🚀 Approach & Intuition
Reset start point if tank drops below zero.

### C++ Pseudo-Code
```cpp
int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    if (accumulate(gas.begin(), gas.end(), 0) < accumulate(cost.begin(), cost.end(), 0)) 
        return -1;
        
    int total = 0;
    int start = 0;
    for (int i = 0; i < gas.size(); i++) {
        total += (gas[i] - cost[i]);
        if (total < 0) {
            total = 0;
            start = i + 1;
        }
    }
    return start;
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

- [Hand of Straights](../hand_of_straights/PROBLEM.md) — Next in category
- [Jump Game II](../jump_game_ii/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
