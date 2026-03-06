# 🔍 Topic Overview: Sorting & Searching

Sorting and Searching are the core efficiency drivers in DSA. Beyond standard `sort()`, you must master Binary Search variants.

## 🔑 Key Concepts Checklist
- [ ] **Binary Search (Variants):** Search in rotated, search range, search on answer (Binary Search on Values).
- [ ] **Merge Sort:** Divide and conquer, stable sorting, counting inversions.
- [ ] **Quick Sort/Select:** Partitioning logic, finding $k$-th smallest in $O(N)$.
- [ ] **Custom Comparators:** Sorting based on multiple criteria or object properties.

## 🎯 Essential Problem Checklist (95% Coverage)
| Problem | Key Concept | Difficulty |
| :--- | :--- | :--- |
| **Binary Search** | Standard Iteration | Easy |
| **Search in Rotated Sorted Array** | Binary Search (Pivot logic) | Medium |
| **First and Last Position** | Binary Search (Lower/Upper bound) | Medium |
| **Search a 2D Matrix** | Binary Search (Coordinate mapping) | Medium |
| **K-th Largest Element** | Quick Select | Medium |
| **Merge Intervals** | Sorting + Greedy | Medium |
| **Median of Two Sorted Arrays** | Binary Search (Partitioning) | Hard |
| **Split Array Largest Sum** | Binary Search on Answer | Hard |

## 🚀 Key Pattern: Binary Search on Answer
Used when you need to find a value $x$ such that a condition is met, and the search space is monotonic.
```cpp
int low = min_val, high = max_val, ans = -1;
while (low <= high) {
    int mid = low + (high - low) / 2;
    if (isValid(mid)) {
        ans = mid;
        high = mid - 1; // Try smaller for minimum
    } else {
        low = mid + 1;
    }
}
```

## 📚 Recommended Reading (CP-Algorithms)
- [Binary Search](https://cp-algorithms.com/num_methods/binary_search.html)
- [Searching for a value in an array](https://cp-algorithms.com/others/binary_search.html)
- [Randomized QuickSelect](https://cp-algorithms.com/others/quick_select.html)
