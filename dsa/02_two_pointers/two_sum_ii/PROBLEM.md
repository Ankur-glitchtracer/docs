#  🎯 Two Pointers: Two Sum II - Input Array Is Sorted

## 📝 Description
[LeetCode 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^5 \le nums[i] \le 10^5$

## 🧠 The Engineering Story

**The Villain:** "The Hash Map Overkill." Using $O(N)$ space when the input is already sorted. Or worse, sticking to the $O(N^2)$ brute force.

**The Hero:** "The Conditional Squeeze." Since the array is sorted, we know exactly how to adjust our sum.

**The Plot:**

1. Initialize `left = 0`, `right = n - 1`.
2. Calculate `current_sum = numbers[left] + numbers[right]`.
3. If `current_sum > target`: We need a smaller sum. Decrement `right`.
4. If `current_sum < target`: We need a larger sum. Increment `left`.
5. If match, return indices (1-based).

**The Twist (Failure):** **The Indexing.** The problem asks for 1-based indexing, a classic "read the requirements" trap.

**Interview Signal:** Leveraging **Sorted Inputs** for optimization.

## 🚀 Approach & Intuition
Use sorted property to converge on the target sum.

### C++ Pseudo-Code
```cpp
vector<int> twoSum(vector<int>& numbers, int target) {
    int l = 0, r = numbers.size() - 1;
    while (l < r) {
        int sum = numbers[l] + numbers[r];
        if (sum == target) return {l + 1, r + 1};
        else if (sum < target) l++;
        else r--;
    }
    return {};
}
```

### Key Observations:

- Two-pointer techniques are often used on sorted arrays to find pairs or triplets in $O(N)$ or $O(N^2)$ time.
- Converging pointers (left and right) are useful for searching, while fast/slow pointers are great for linked lists.

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

- **Harder Variant:** Can this be extended to 3 pointers or $K$ pointers? How would the complexity change?
- **Scale Question:** If the data is stored in a linked list on disk, how can you minimize seek time while moving pointers?
- **Edge Case Probe:** What if the pointers meet immediately? What if the array has only one or two elements?

## 🔗 Related Problems

- [3Sum](../3sum/PROBLEM.md) — Next in category
- [Valid Palindrome](../valid_palindrome/PROBLEM.md) — Previous in category
- [Best Time to Buy/Sell Stock](../../03_sliding_window/best_time_to_buy_sell_stock/PROBLEM.md) — Prerequisite for Sliding Window
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
