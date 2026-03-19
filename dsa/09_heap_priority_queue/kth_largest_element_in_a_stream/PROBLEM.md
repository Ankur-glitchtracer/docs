---
impact: "Easy"
nr: false
confidence: 2
---
# 📊 Heap: Kth Largest Element in a Stream

## 📝 Description
[LeetCode 703](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
Design a class to find the `k`th largest element in a stream. Note that it is the `k`th largest element in the sorted order, not the `k`th distinct element.

!!! info "Real-World Application"
    Used in **Leaderboards** (keeping track of the top 10 scores), **Network Monitoring** (tracking top K bandwidth consumers), and **Anomaly Detection** (thresholding).

## 🛠️ Constraints & Edge Cases
- $1 \le k \le 10^4$
- $0 \le nums.length \le 10^4$
- **Edge Cases to Watch:**
    - Initial array size < k (must assume valid `add` calls will follow).
    - Negative numbers.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    To find the $K^{th}$ largest element, we don't need to keep the *entire* history sorted. We only care about the "Top K" elements. If we have the Top K elements, the $K^{th}$ largest is simply the **smallest** of that group. A **Min-Heap** of size K is perfect for this.

### 🐢 Brute Force (Naive)
Append to list and sort every time `add()` is called.
- **Time Complexity:** $O(N \log N)$ per call.

### 🐇 Optimal Approach (Min-Heap)
1.  Maintain a Min-Heap.
2.  If heap size < `k`, push `val`.
3.  If heap size == `k` and `val > heap.top()`:
    - Pop small root.
    - Push new `val`.
4.  The root of the heap is always the $K^{th}$ largest.

### 🧩 Visual Tracing
```mermaid
graph TD
    A[Stream, K=3]
    B[Add 4] --> H1[4]
    C[Add 5] --> H2[4, 5]
    D[Add 8] --> H3[4, 5, 8] -> Result: 4
    E[Add 2] -->|2 < 4| H3 -> Result: 4
    F[Add 10] -->|10 > 4| H4[5, 8, 10] -> Result: 5
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log K)$ — Per `add` operation.
- **Space Complexity:** $\mathcal{O}(K)$ — Store top K elements.

---

## 🎤 Interview Toolkit

- **Question:** Why Min-Heap for Kth *Largest*? (Because we want to efficiently evict the smallest of the top group to make room for larger ones, and Min-Heap gives access to the minimum in $O(1)$).

## 🔗 Related Problems
- [Kth Largest Element in an Array](../kth_largest_element_in_an_array/PROBLEM.md) — Static version
- [Top K Frequent Elements](../../01_arrays_hashing/top_k_frequent_elements/PROBLEM.md) — Related
