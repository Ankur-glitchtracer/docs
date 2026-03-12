#  🃏 Sorting: Insertion Sort

## 📝 Description
Implement Insertion Sort to sort an array of integers in ascending order.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 5 \cdot 10^4$
- Values can be large, requiring $O(N \log N)$ sorting.

## 🧠 The Engineering Story

**The Villain:** "The Unsorted Hand." Like a player receiving cards one by one, you need to place each new card in its correct position relative to the cards already in your hand.

**The Hero:** "The Squeezing Inserter." Pick an element and shift all larger elements one position to the right to make a "hole" for it.

**The Plot:**

1. Assume the first element is sorted.
2. For each subsequent element:
   - Store it as `key`.
   - Move backwards through the sorted portion.
   - Shift elements right if they are larger than `key`.
   - Insert `key` into the vacated spot.

**The Twist (Failure):** **The Shift Overwrite.** Overwriting an element before you've shifted it. Always store the `key` first.

**Interview Signal:** Mastery of **Online Sorting** (sorting as data arrives).

## 🚀 Approach & Intuition
Build the sorted array one item at a time.

### C++ Pseudo-Code
```cpp
void insertionSort(vector<int>& nums) {
    int n = nums.size();
    for (int i = 1; i < n; i++) {
        int key = nums[i];
        int j = i - 1;
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = key;
    }
}
```

### Key Observations:

- Understand the stability and space-time trade-offs between Merge Sort ($O(N \log N)$ space) and Quick Sort ($O(1)$ space).
- For small datasets or specialized constraints, $O(N)$ algorithms like Counting Sort or Radix Sort may be applicable.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2)$ (Average/Worst), $O(N)$ (Best - nearly sorted)
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

- [Selection Sort](../selection_sort/PROBLEM.md) — Next in category
- [Bubble Sort](../bubble_sort/PROBLEM.md) — Previous in category
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
