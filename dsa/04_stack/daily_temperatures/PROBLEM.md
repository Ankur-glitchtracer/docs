#  🌡️ Stack: Daily Temperatures

## 📝 Description
[LeetCode 739](https://leetcode.com/problems/daily-temperatures/)
Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0`.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- Constraints vary depending on the specific stack application.

## 🧠 The Engineering Story

**The Villain:** "The Future Look-ahead." For each day, looking ahead to find the next warmer day ($O(N^2)$).

**The Hero:** "The Monotonic Stack." We store indices of days with *decreasing* temperatures. Why? Because if today is warmer than the day on top of the stack, today is the answer for that previous day!

**The Plot:**

1. Iterate through temperatures.
2. While `current_temp > stack.top_temp()`:
   - This means we found a warmer day for the day at the top of the stack.
   - Pop the index.
   - Calculate `wait_days = current_index - popped_index`.
   - Update result.
3. Push current index.

**The Twist (Failure):** **The Leftovers.** Indices left in the stack at the end have no warmer future day. Their result remains 0 (default).

**Interview Signal:** Recognizing the **Next Greater Element** pattern.

## 🚀 Approach & Intuition
Store indices. Pop when a warmer temperature is found.

### C++ Pseudo-Code
```cpp
vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> res(n, 0);
    stack<int> s; // stores indices
    
    for (int i = 0; i < n; i++) {
        while (!s.empty() && temperatures[i] > temperatures[s.top()]) {
            int prevIndex = s.top(); s.pop();
            res[prevIndex] = i - prevIndex;
        }
        s.push(i);
    }
    return res;
}
```

### Key Observations:

- Stacks are essential for problems involving nested structures, like parentheses or expression evaluation.
- Monotonic stacks are a powerful variation used to find the next greater or smaller element in $O(N)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
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

- [Car Fleet](../car_fleet/PROBLEM.md) — Next in category
- [Generate Parentheses](../generate_parentheses/PROBLEM.md) — Previous in category
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
