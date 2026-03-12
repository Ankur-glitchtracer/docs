#  🪟 Sliding Window: Sliding Window Maximum

## 📝 Description
[LeetCode 239](https://leetcode.com/problems/sliding-window-maximum/)
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

## 🛠️ Requirements/Constraints

- $1 \le s.length \le 10^5$
- $s$ consists of standard ASCII characters.

## 🧠 The Engineering Story

**The Villain:** "The Repeated Max." Recalculating `max(window)` every time takes $O(k)$. Total time $O(N \cdot k)$. If $k \approx N$, this is $O(N^2)$.

**The Hero:** "The Monotonic Queue (Deque)." We need a structure that gives us the max in $O(1)$ and supports adding/removing from both ends.

**The Plot:**

1. Use a Deque to store *indices*.
2. **Maintain Decreasing Order:** When adding `nums[i]`, pop all elements from the back of the deque that are smaller than `nums[i]` (they can never be the max anymore).
3. **Remove Outdated:** If the front index is out of the current window (`i - k`), pop it.
4. The front of the deque is always the index of the max element for the current window.

**The Twist (Failure):** **Storing Values vs Indices.** Storing values makes it hard to know *when* an element leaves the window. Always store indices.

**Interview Signal:** Mastery of **Monotonic Queues**.

## 🚀 Approach & Intuition
Maintain indices of elements in decreasing order of their values.

### C++ Pseudo-Code
```cpp
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;
    vector<int> res;
    
    for (int i = 0; i < nums.size(); i++) {
        // Remove indices out of window
        if (!dq.empty() && dq.front() == i - k) 
            dq.pop_front();
            
        // Maintain decreasing order
        while (!dq.empty() && nums[dq.back()] < nums[i])
            dq.pop_back();
            
        dq.push_back(i);
        
        if (i >= k - 1)
            res.push_back(nums[dq.front()]);
    }
    return res;
}
```

### Key Observations:

- Maintain a window that satisfies a certain condition and expand/contract it as you iterate.
- Use a Hash Map or Frequency Array to track elements within the current window in $O(1)$ time.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(K)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the window size is not fixed, or we need to find the count of all windows satisfying a condition?
- **Scale Question:** In a streaming context (e.g., Flink or Spark Streaming), how would you maintain the window state efficiently?
- **Edge Case Probe:** How do you handle cases where no window satisfies the condition? What about very small inputs?

## 🔗 Related Problems

- [Minimum Window Substring](../minimum_window_substring/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
