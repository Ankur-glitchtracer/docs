#  📊 Stack: Largest Rectangle in Histogram

## 📝 Description
[LeetCode 84](https://leetcode.com/problems/largest-rectangle-in-histogram/)
Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- Constraints vary depending on the specific stack application.

## 🧠 The Engineering Story

**The Villain:** "The Expanding Width." For every bar, expanding left and right to find the limit ($O(N^2)$).

**The Hero:** "The Monotonic Increasing Stack." We maintain indices of bars with increasing heights.

**The Plot:**

1. Iterate through bars.
2. If `current_height < stack.top_height`: The bar at `stack.top` cannot extend further right. It's time to process it.
   - Pop the top. This is the `height`.
   - The `width` is `i - stack.top() - 1` (distance between current index and the *new* top).
   - `area = height * width`.
3. Push current index.

**The Twist (Failure):** **The Leftover Bars.** After the loop, the stack isn't empty. These bars extend all the way to the end. You must process them with `width = n - stack.top() - 1`.

**Interview Signal:** Mastery of **Hard Monotonic Stack** problems.

## 🚀 Approach & Intuition
Find the nearest smaller element to the left and right for every bar.

### C++ Pseudo-Code
```cpp
int largestRectangleArea(vector<int>& heights) {
    stack<int> s;
    heights.push_back(0); // Dummy bar to clear stack at end
    int maxArea = 0;
    
    for (int i = 0; i < heights.size(); i++) {
        while (!s.empty() && heights[i] < heights[s.top()]) {
            int h = heights[s.top()]; s.pop();
            int w = s.empty() ? i : i - s.top() - 1;
            maxArea = max(maxArea, h * w);
        }
        s.push(i);
    }
    return maxArea;
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

- [Car Fleet](../car_fleet/PROBLEM.md) — Previous in category
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
