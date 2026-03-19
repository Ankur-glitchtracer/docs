---
impact: "Medium"
nr: false
confidence: 2
---
# 🔝 Heap: Kth Largest Element in an Array

## 📝 Description
[LeetCode 215](https://leetcode.com/problems/kth-largest-element-in-an-array/)
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element. You must solve it in $O(N)$ time complexity.

!!! info "Real-World Application"
    Used in **Order Statistics**, finding medians, or selecting top candidates without fully sorting a massive dataset.

## 🛠️ Constraints & Edge Cases
- $1 \le k \le nums.length \le 10^5$
- **Edge Cases to Watch:**
    - Array is already sorted or reverse sorted.
    - Duplicates.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    Sorting is $O(N \log N)$. A Min-Heap of size K is $O(N \log K)$. To get $O(N)$, we need **QuickSelect** (partitioning logic from QuickSort). By partitioning, we place one element (the pivot) in its correct final sorted position. If that position is `N-K`, we are done! If not, we only recurse into *one* half.

### 🐢 Brute Force (Naive)
Sort and pick index `N-k`.
- **Time Complexity:** $O(N \log N)$.

### 🐇 Optimal Approach (QuickSelect)
1.  Choose a pivot (randomly to avoid worst case).
2.  Partition array: elements <= pivot to left, > pivot to right.
3.  Pivot ends at index `p`.
4.  Target index is `N - k` (if sorting ascending).
5.  If `p == target`: return `nums[p]`.
6.  If `p < target`: Recurse Right.
7.  If `p > target`: Recurse Left.

### 🧩 Visual Tracing
```mermaid
graph TD
    A[Arr: 3,2,1,5,6,4, K=2 (Target Idx 4)]
    B[Pivot: 4] -->|Partition| C[3,2,1, 4 , 5,6]
    C -->|4 is at Idx 3 < Target 4| RecurseRight
    D[Right Sub: 5, 6] -->|Pivot 5| E[5, 6]
    E -->|5 is at Idx 4 == Target| Return 5
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N)$ average, $\mathcal{O}(N^2)$ worst case (without random pivot).
- **Space Complexity:** $\mathcal{O}(1)$ (Iterative) or $\mathcal{O}(\log N)$ (Recursive stack).

---

## 🎤 Interview Toolkit

- **Comparison:** Min-Heap solution is more stable $O(N \log K)$ and easier to implement correctly. QuickSelect is faster on average but tricky.
- **Libraries:** Python's `heapq.nlargest` is $O(N \log K)$.

## 🔗 Related Problems
- [Kth Largest in Stream](../kth_largest_element_in_a_stream/PROBLEM.md) — Streaming version
