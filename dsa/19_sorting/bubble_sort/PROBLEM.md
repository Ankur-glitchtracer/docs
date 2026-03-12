#  🫧 Sorting: Bubble Sort

## 📝 Description
Implement Bubble Sort to sort an array of integers in ascending order.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 5 \cdot 10^4$
- Values can be large, requiring $O(N \log N)$ sorting.

## 🧠 The Engineering Story

**The Villain:** "The Chaos Array." Elements are in random order. You want to bring order with the simplest possible logic.

**The Hero:** "The Bubbling Buoyancy." Larger elements "bubble up" to the end of the array in each pass.

**The Plot:**

1. Compare adjacent elements `(i, i+1)`.
2. If `left > right`, swap them.
3. Repeat this for the whole array. After 1 pass, the largest element is at the end.
4. Repeat for $N-1$ passes.

**The Twist (Failure):** **The Infinite Loop.** Forgetting to stop early if no swaps occurred in a pass (meaning the array is already sorted).

**Interview Signal:** Understanding of **Basic Iterative Sorting** and best-case optimization.

## 🚀 Approach & Intuition
Repeatedly step through the list, compare adjacent elements and swap them if they are in the wrong order.

### C++ Pseudo-Code
```cpp
void bubbleSort(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                swap(nums[j], nums[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}
```

### Key Observations:

- Understand the stability and space-time trade-offs between Merge Sort ($O(N \log N)$ space) and Quick Sort ($O(1)$ space).
- For small datasets or specialized constraints, $O(N)$ algorithms like Counting Sort or Radix Sort may be applicable.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2)$ (Average/Worst), $O(N)$ (Best with optimization)
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you make the sort 'Stable'? What if you need to sort elements that don't fit in memory (External Sort)?
- **Scale Question:** How would you implement a distributed sort (like Terabyte Sort) using multiple machines?
- **Edge Case Probe:** How does the algorithm perform on already sorted, reverse-sorted, or all-identical element arrays?

## 🔗 Related Problems

- [Insertion Sort](../insertion_sort/PROBLEM.md) — Next in category
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
