#  ⚡ Sorting: Quick Sort

## 📝 Description
Implement Quick Sort to sort an array of integers in ascending order. Compare Lomuto and Hoare partition schemes.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 5 \cdot 10^4$
- Values can be large, requiring $O(N \log N)$ sorting.

## 🧠 The Engineering Story

**The Villain:** "The Pivot Choice." Choosing a bad pivot (like the first element of a sorted array) can turn this $O(N \log N)$ hero into an $O(N^2)$ villain.

**The Hero:** "The Partition Master." Reorganize the array around a pivot such that everything to the left is smaller and everything to the right is larger.

**The Plot:**

1. Pick a `pivot` (last, middle, or random).
2. **Lomuto Partition:** Use one pointer to track the "boundary" of smaller elements. Easy to code.
3. **Hoare Partition:** Use two pointers from both ends moving inward. Faster and more efficient swaps.
4. Recursively sort the two partitions.

**The Twist (Failure):** **The Stack Overflow.** Deep recursion on skewed partitions. Using tail-call optimization or picking a random pivot helps.

**Interview Signal:** Mastery of **In-Place Partitioning** and **QuickSelect** fundamentals.

## 🚀 Approach & Intuition
Partition around a pivot and recurse.

### C++ Pseudo-Code (Lomuto Partition)
```cpp
int partitionLomuto(vector<int>& nums, int low, int high) {
    int pivot = nums[high];
    int i = low;
    for (int j = low; j < high; j++) {
        if (nums[j] < pivot) {
            swap(nums[i++], nums[j]);
        }
    }
    swap(nums[i], nums[high]);
    return i;
}
```

### C++ Pseudo-Code (Hoare Partition)
```cpp
int partitionHoare(vector<int>& nums, int low, int high) {
    int pivot = nums(To be detailed...);
    int i = low - 1, j = high + 1;
    while (true) {
        do { i++; } while (nums[i] < pivot);
        do { j--; } while (nums[j] > pivot);
        if (i >= j) return j;
        swap(nums[i], nums[j]);
    }
}
```

### Key Observations:

- Understand the stability and space-time trade-offs between Merge Sort ($O(N \log N)$ space) and Quick Sort ($O(1)$ space).
- For small datasets or specialized constraints, $O(N)$ algorithms like Counting Sort or Radix Sort may be applicable.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$ (Average), $O(N^2)$ (Worst case - rare with good pivot)
    - **Space Complexity:** $O(\log N)$ (Recursion stack)

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

- [Merge Sort](../merge_sort/PROBLEM.md) — Previous in category
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
