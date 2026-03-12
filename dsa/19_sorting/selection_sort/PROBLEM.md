#  🎯 Sorting: Selection Sort

## 📝 Description
Implement Selection Sort to sort an array of integers in ascending order.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 5 \cdot 10^4$
- Values can be large, requiring $O(N \log N)$ sorting.

## 🧠 The Engineering Story

**The Villain:** "The Hidden Minimum." You need to find the absolute smallest element in a mess of numbers.

**The Hero:** "The Minimum Scout." In each pass, find the smallest element in the unsorted portion and swap it to the front.

**The Plot:**

1. Iterate `i` from 0 to $N-1$.
2. Assume `i` is the `min_index`.
3. Scan from `i+1` to $N$. If `nums[j] < nums[min_index]`, update `min_index`.
4. Swap `nums[i]` with `nums[min_index]`.

**The Twist (Failure):** **The Stability.** Selection sort is generally NOT stable because swaps can jump over identical elements.

**Interview Signal:** Understanding **Minimum Selection** logic.

## 🚀 Approach & Intuition
Repeatedly find the minimum element from the unsorted part and put it at the beginning.

### C++ Pseudo-Code
```cpp
void selectionSort(vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (nums[j] < nums[minIdx]) minIdx = j;
        }
        swap(nums[i], nums[minIdx]);
    }
}
```

### Key Observations:

- Understand the stability and space-time trade-offs between Merge Sort ($O(N \log N)$ space) and Quick Sort ($O(1)$ space).
- For small datasets or specialized constraints, $O(N)$ algorithms like Counting Sort or Radix Sort may be applicable.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N^2)$ (Always - doesn't care if sorted)
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

- [Merge Sort](../merge_sort/PROBLEM.md) — Next in category
- [Insertion Sort](../insertion_sort/PROBLEM.md) — Previous in category
- [Binary Search](../../05_binary_search/binary_search/PROBLEM.md) — Prerequisite for Binary Search
- [Contains Duplicate](../../01_arrays_hashing/contains_duplicate/PROBLEM.md) — Prerequisite: Arrays & Hashing
