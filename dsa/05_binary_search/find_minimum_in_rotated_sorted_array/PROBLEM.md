#  📉 Binary Search: Find Minimum in Rotated Sorted Array

## 📝 Description
[LeetCode 153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Target value is within the range of the data type.

## 🧠 The Engineering Story

**The Villain:** "The Linear Scan." Just iterating to find the min takes $O(N)$. We want logarithmic time.

**The Hero:** "The Cliff Diver." We are looking for the point where the numbers drop (the pivot).

**The Plot:**

1. `low = 0`, `high = n - 1`.
2. If `nums[low] < nums[high]`, the array is already sorted. Return `nums[low]`.
3. Pick `mid`.
4. If `nums[mid] > nums[right]`: The left side is sorted, but the "cliff" (min) is to the *right*. Go right (`low = mid + 1`).
5. Else (`nums[mid] <= nums[right]`): The pivot is to the *left* (or at mid). Go left (`high = mid`). Note: we don't do `mid - 1` because `mid` could be the min.

**The Twist (Failure):** **The Pivot Logic.** It's slightly different from finding a target. We compare against `right` boundary, not `target`.

**Interview Signal:** Modifying standard **Binary Search Conditions**.

## 🚀 Approach & Intuition
If `mid > right`, the min is to the right. Else, it's to the left/current.

### C++ Pseudo-Code
```cpp
int findMin(vector<int>& nums) {
    int l = 0, r = nums.size() - 1;
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] > nums[r]) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return nums[l];
}
```

### Key Observations:

- Binary search can be applied not just to sorted arrays, but to any monotonic search space (Search on Answer).
- Be careful with the boundaries ($left, right$) and the condition for moving them to avoid infinite loops.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log N)$
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you apply 'Binary Search on Answer' to solve optimization problems (e.g., minimize max distance)?
- **Scale Question:** If you are searching in a distributed database, how can you reduce the number of network round trips?
- **Edge Case Probe:** Does your mid-point calculation `(left + right) / 2` overflow for very large indices?

## 🔗 Related Problems

- [Search in Rotated Array](../search_in_rotated_sorted_array/PROBLEM.md) — Next in category
- [Koko Eating Bananas](../koko_eating_bananas/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
