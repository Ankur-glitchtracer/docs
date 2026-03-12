#  🚗 Stack: Car Fleet

## 📝 Description
[LeetCode 853](https://leetcode.com/problems/car-fleet/)
There are `n` cars going to the same destination along a one-lane road. The destination is at position `target`. You are given two arrays `position` and `speed`. A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The distance between these two cars is ignored - they are assumed to have the same position. A car fleet is some non-empty set of cars driving at the same position and same speed. Return the number of car fleets that will arrive at the destination.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- Constraints vary depending on the specific stack application.

## 🧠 The Engineering Story

**The Villain:** "The Physics Simulation." Simulating the cars second-by-second to see who collides. Slow and messy.

**The Hero:** "The Time-to-Target Analyzer." Calculate *when* each car would reach the target if the road were empty (`(target - pos) / speed`).

**The Plot:**

1. Combine `position` and `speed` into pairs and sort by position (closest to target first).
2. Iterate from closest to farthest (reverse order).
3. Calculate `time_to_reach`.
4. If a car behind takes *less* time than the car in front, it will catch up. It joins the fleet (don't increment count).
5. If it takes *more* time, it starts a new fleet (increment count, update `current_slowest_time`).

**The Twist (Failure):** **Floating Point Precision.** Time is a float. Be careful with direct equality checks, though usually fine here.

**Interview Signal:** Sorting combined with **Greedy Grouping**.

## 🚀 Approach & Intuition
Sort by position descending. Compare arrival times.

### C++ Pseudo-Code
```cpp
int carFleet(int target, vector<int>& position, vector<int>& speed) {
    int n = position.size();
    vector<pair<int, double>> cars;
    for (int i = 0; i < n; i++) {
        double time = (double)(target - position[i]) / speed[i];
        cars.push_back({position[i], time});
    }
    sort(cars.rbegin(), cars.rend());
    
    int fleets = 0;
    double maxTime = 0.0;
    for (int i = 0; i < n; i++) {
        if (cars[i].second > maxTime) {
            fleets++;
            maxTime = cars[i].second;
        }
    }
    return fleets;
}
```

### Key Observations:

- Stacks are essential for problems involving nested structures, like parentheses or expression evaluation.
- Monotonic stacks are a powerful variation used to find the next greater or smaller element in $O(N)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$ (Sorting)
    - **Space Complexity:** $O(N)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you solve this using a single pass or by transforming the problem into a Monotonic Stack problem?
- **Scale Question:** If the stack needs to be persistent (undo/redo functionality), how would you implement it using a functional data structure?
- **Edge Case Probe:** What happens on an empty stack or when the input contains unexpected characters?

## 🔗 Related Problems

- [Largest Rectangle in Histogram](../largest_rectangle_in_histogram/PROBLEM.md) — Next in category
- [Daily Temperatures](../daily_temperatures/PROBLEM.md) — Previous in category
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
