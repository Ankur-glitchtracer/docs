---
impact: "Medium"
nr: false
confidence: 2
---
# 🎯 Heap: K Closest Points to Origin

## 📝 Description
[LeetCode 973](https://leetcode.com/problems/k-closest-points-to-origin/)
Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`. The distance between two points on the X-Y plane is the Euclidean distance (i.e., $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$).

!!! info "Real-World Application"
    Basis for **K-Nearest Neighbors (KNN)** algorithms in Machine Learning, and **Geo-spatial Search** (e.g., finding the 5 closest Uber drivers or restaurants).

## 🛠️ Constraints & Edge Cases
- $1 \le k \le \text{points.length} \le 10^4$
- $-10^4 < x_i, y_i < 10^4$
- **Edge Cases to Watch:**
    - `k = N` (Return all points).
    - `k = 1`.
    - Multiple points with same distance.

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
    We need the K *smallest* distances. If we sort everyone, it's $O(N \log N)$. Can we do better? We only care about the K smallest. We can use a **Max-Heap** of size K. Why Max? Because the top of the Max-Heap is the "largest of the smallest". If a new point is smaller than the top, we pop the top and push the new one.

### 🐢 Brute Force (Naive)
Sort the entire list by distance. Return first K.
- **Time Complexity:** $O(N \log N)$.

### 🐇 Optimal Approach (Max-Heap)
1.  Iterate through all points.
2.  Calculate squared distance $x^2 + y^2$ (avoid sqrt to save precision/time).
3.  Push `(-distance, point)` to heap (simulating Max-Heap in Python).
4.  If heap size > `k`, pop the largest distance (smallest negative).
5.  Remaining heap contains the k closest points.

### 🧩 Visual Tracing
```mermaid
graph TD
    A[Points: (1,3), (-2,2), (5,8), K=2]
    B[Distances: 10, 8, 89]
    C[Heap Push -10] --> H1[-10]
    D[Heap Push -8] --> H2[-10, -8]
    E[Heap Push -89] --> H3[-89, -10, -8]
    F[Size > 2: Pop -89] --> H4[-10, -8]
    G[Result: (1,3), (-2,2)]
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N \log K)$ — We push N items into a heap constrained to size K.
- **Space Complexity:** $\mathcal{O}(K)$ — Heap size.

---

## 🎤 Interview Toolkit

- **Alternative:** QuickSelect (Hoare's Selection) can find the Kth element in $O(N)$ average time, but worst case $O(N^2)$.
- **Math Trick:** Don't use `sqrt()`. Comparing squared distances is sufficient and faster.

## 🔗 Related Problems
- [Kth Largest Element in an Array](../kth_largest_element_in_an_array/PROBLEM.md) — Previous in category
- [Top K Frequent Elements](../../01_arrays_hashing/top_k_frequent_elements/PROBLEM.md) — Related Top-K pattern
