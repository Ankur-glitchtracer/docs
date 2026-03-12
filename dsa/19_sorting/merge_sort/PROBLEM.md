#  🧶 Sorting: Merge Sort

## 📝 Description
Implement Merge Sort to sort an array of integers in ascending order.

## 🛠️ Requirements/Constraints

- Implement an efficient $O(N \log N)$ sorting algorithm.
- Handle arrays of various sizes including 0 and 1.

## 🧠 The Engineering Story

**The Villain:** "The Scale Demon." $O(N^2)$ algorithms fail when $N=1,000,000$. We need a Divide and Conquer strategy.

**The Hero:** "The Great Merger." Recursively split the array in half until you have single elements, then merge them back in sorted order.

**The Plot:**

1. **Divide:** Find the midpoint. `mergeSort(left)`, `mergeSort(right)`.
2. **Conquer:** The base case is an array of size 1 (already sorted).
3. **Combine (Merge):**
   - Use two pointers to compare elements from the two sorted halves.
   - Pick the smaller one and add to a temporary array.
   - Copy the temp array back to the original.

**The Twist (Failure):** **The Memory Tax.** Merge sort is not in-place ($O(N)$ space). If memory is tight, Quick Sort is preferred.

**Interview Signal:** Mastery of **Divide and Conquer** and **Stable Sorting**.

## 🚀 Approach & Intuition
Merge Sort is a quintessential divide-and-conquer algorithm. It breaks the problem into smaller sub-problems (sorting halves), solves them recursively, and then combines the results (merging sorted lists).

### Key Observations:

- It is a stable sort (preserves relative order of equal elements).
- Unlike Quick Sort, it has a guaranteed $O(N \log N)$ time complexity.
- The merging process is where the actual sorting happens.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$ - The array is split $\log N$ times, and each level of merging takes $O(N)$ time.
    - **Space Complexity:** $O(N)$ - Temporary arrays are required for the merge step.

## 💻 Solution Implementation

```python
--8<-- "dsa/19_sorting/merge_sort/solution.py"
```

!!! success "Aha! Moment"
    Sorting two already-sorted lists is much easier ($O(N)$) than sorting an unsorted list. By recursively breaking the list down to single elements (which are inherently sorted), we can build back up using only this efficient merge operation.

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you make the sort 'Stable'? What if you need to sort elements that don't fit in memory (External Sort)?
- **Scale Question:** How would you implement a distributed sort (like Terabyte Sort) using multiple machines?
- **Edge Case Probe:** How does the algorithm perform on already sorted, reverse-sorted, or all-identical element arrays?

## 🔗 Related Problems

- [Quick Sort](../quick_sort/PROBLEM.md) — Next in category
- [Selection Sort](../selection_sort/PROBLEM.md) — Previous in category
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
