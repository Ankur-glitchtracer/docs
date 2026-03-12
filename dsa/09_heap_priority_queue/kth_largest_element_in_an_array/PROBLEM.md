#  🔝 Heap: Kth Largest Element in an Array

## 📝 Description
[LeetCode 215](https://leetcode.com/problems/kth-largest-element-in-an-array/)
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element. You must solve it in $O(N)$ time complexity.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^4 \le nums[i] \le 10^4$

## 🧠 The Engineering Story

**The Villain:** "The Sorting Crutch." Just calling `sort()` is easy ($O(N \log N)$), but interviewers know it's not optimal for finding just *one* element.

**The Hero:** "QuickSelect (or Min-Heap)."

**The Plot:**

1. (To be detailed...)
2. (To be detailed...)

**The Twist (Failure):** **Worst Case.** QuickSelect can degrade to $O(N^2)$ if already sorted. Random shuffling or "Median of Medians" fixes this.

**Interview Signal:** Mastery of **Partitioning Algorithms**.

## 🚀 Approach & Intuition
Partitioning until the pivot lands at index `n - k`.

### C++ Pseudo-Code
```cpp
int findKthLargest(vector<int>& nums, int k) {
    int target = nums.size() - k;
    int l = 0, r = nums.size() - 1;
    
    while (l <= r) {
        int pivot = partition(nums, l, r);
        if (pivot == target) return nums[pivot];
        if (pivot < target) l = pivot + 1;
        else r = pivot - 1;
    }
    return -1;
}

int partition(vector<int>& nums, int l, int r) {
    int pivot = nums[r];
    int p = l;
    for (int i = l; i < r; i++) {
        if (nums[i] <= pivot) {
            swap(nums[i], nums[p]);
            p++;
        }
    }
    swap(nums[p], nums[r]);
    return p;
}
```

### Key Observations:

- Heaps are the go-to for finding the $K$-th largest or smallest element in $O(N \log K)$ time.
- Use a Min-Heap for $K$ largest elements and a Max-Heap for $K$ smallest elements to optimize space.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ (Average)
    - **Space Complexity:** $O(1)$ (Iterative QuickSelect)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you implement a custom Heap from scratch? How would you implement a 'Decrease Key' operation?
- **Scale Question:** How would you maintain a Top-K list across 100 machines with frequent updates?
- **Edge Case Probe:** What if all elements have the same priority? How do you handle empty heap extractions?

## 🔗 Related Problems

- [Task Scheduler](../task_scheduler/PROBLEM.md) — Next in category
- [K Closest Points](../k_closest_points_to_origin/PROBLEM.md) — Previous in category
- [Reconstruct Itinerary](../../12_advanced_graphs/reconstruct_itinerary/PROBLEM.md) — Prerequisite for Advanced Graphs
- [Maximum Subarray](../../15_greedy/maximum_subarray/PROBLEM.md) — Prerequisite for Greedy
