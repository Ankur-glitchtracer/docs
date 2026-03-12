#  📊 Binary Search: Median of Two Sorted Arrays

## 📝 Description
[LeetCode 4](https://leetcode.com/problems/median-of-two-sorted-arrays/)
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be $O(\log (m+n))$.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Target value is within the range of the data type.

## 🧠 The Engineering Story

**The Villain:** "The Linear Merge." Merging the two arrays into one big array takes $O(M+N)$ time and space. Too slow/heavy.

**The Hero:** "The Virtual Partition." We want to cut both arrays such that the left half contains exactly half the total elements, and every element on the left is smaller than every element on the right.

**The Plot:**

1. Perform binary search on the *smaller* array (say `A`).
2. Partition `A` at `i`. This forces a partition at `j` in `B` such that `i + j = total_half`.
3. Check validity:
   - `A[i-1] <= B[j]` (Left A < Right B)
   - `B[j-1] <= A[i]` (Left B < Right A)
4. If valid, calculate median from the boundary values.
5. If not, adjust binary search range.

**The Twist (Failure):** **The Edge Cases.** Partitioning at index 0 or `len` (empty left or right parts). Use infinity/negative-infinity to handle these boundaries cleanly.

**Interview Signal:** Mastery of **Hard** binary search and array partitioning.

## 🚀 Approach & Intuition
Find the correct split point in the smaller array.

### C++ Pseudo-Code
```cpp
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);
    
    int x = nums1.size(), y = nums2.size();
    int l = 0, r = x;
    
    while (l <= r) {
        int partX = (l + r) / 2;
        int partY = (x + y + 1) / 2 - partX;
        
        int maxLeftX = (partX == 0) ? INT_MIN : nums1[partX - 1];
        int minRightX = (partX == x) ? INT_MAX : nums1[partX];
        int maxLeftY = (partY == 0) ? INT_MIN : nums2[partY - 1];
        int minRightY = (partY == y) ? INT_MAX : nums2[partY];
        
        if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
            if ((x + y) % 2 == 0)
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0;
            else
                return max(maxLeftX, maxLeftY);
        } else if (maxLeftX > minRightY) {
            r = partX - 1;
        } else {
            l = partX + 1;
        }
    }
    return 0.0;
}
```

### Key Observations:

- Binary search can be applied not just to sorted arrays, but to any monotonic search space (Search on Answer).
- Be careful with the boundaries ($left, right$) and the condition for moving them to avoid infinite loops.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(\log(\min(M, N)))$
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

- [Time Based KV Store](../time_based_key_value_store/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
- [Bubble Sort](../../19_sorting/bubble_sort/PROBLEM.md) — Prerequisite: Sorting
