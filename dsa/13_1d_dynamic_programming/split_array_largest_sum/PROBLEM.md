---
impact: "High"
nr: false
confidence: 4
-------------

# 📦 Binary Search: Split Array Largest Sum

## 📝 Problem Description

Given an array `nums` consisting of non-negative integers and an integer `k`, split the array into `k` or fewer **contiguous subarrays** such that the **largest sum among these subarrays is minimized**.

Return the minimized largest sum.

[LeetCode 410](https://leetcode.com/problems/split-array-largest-sum/)

!!! info "Real-World Application"
Used in **Workload Partitioning** and **Distributed Systems**. For example, dividing tasks among `k` servers such that the **maximum load on any server is minimized**, ensuring balanced performance.

## 🛠️ Constraints & Edge Cases

* $1 \le nums.length \le 10^3$
* $0 \le nums[i] \le 10^6$
* $1 \le k \le \min(50, nums.length)$
* **Edge Cases to Watch:**

  * $k = 1$ → entire array is one subarray → answer = $\sum nums$
  * $k = nums.length$ → each element is its own subarray → answer = $\max(nums)$
  * Large values in `nums` → must avoid brute force

---

## 🧠 Approach & Intuition

!!! success "The Aha! Moment"
This is a **Binary Search on the Answer** problem. The maximum subarray sum is monotonic: if we can split the array with max sum ≤ `x`, then we can also do it for any `x' > x`.

### 🐢 Brute Force (Naive)

Try all possible ways to split the array into `k` parts and compute the largest sum.

* **Time Complexity:** Exponential
* **Why it fails:** Too many possible partitions → infeasible

### 🐇 Optimal Approach

Use **Binary Search** on the answer:

1. Search space:

   * `low = max(nums)` (minimum possible largest sum)
   * `high = sum(nums)` (maximum possible largest sum)
2. While `low < high`:

   * Compute `mid`
   * Check if we can split into ≤ `k` subarrays such that no subarray sum exceeds `mid`
3. If possible → try smaller (`high = mid`)
4. Else → increase (`low = mid + 1`)
5. Return `low`

### 🧩 Visual Tracing

```mermaid
graph TD
    A[Range: max(nums) to sum(nums)] --> B{Check max sum mid}
    B -- "Can split into ≤ k" --> C[Search Left: minimize further]
    B -- "Need > k splits" --> D[Search Right: increase limit]
    style C fill:#ccffcc,stroke:#00aa00
    style D fill:#ffcccc,stroke:#aa0000
```

---

## 💻 Solution Implementation

```python
(Implementation details need to be added...)
```

### ⏱️ Complexity Analysis

* **Time Complexity:** $\mathcal{O}(N \log(\sum nums))$ — Binary search over range, each check is linear
* **Space Complexity:** $\mathcal{O}(1)$ — Constant extra space

---

## 🎤 Interview Toolkit

* **Greedy Insight:** Always pack elements into current subarray until exceeding limit, then split
* **Why max(nums)?** The largest element must be in some subarray → lower bound
* **Why sum(nums)?** No split case → upper bound
* **Pattern Recognition:** Classic **minimize maximum** → think binary search

## 🔗 Related Problems

* [Koko Eating Bananas](../../05_binary_search/koko_eating_bananas/PROBLEM.md) — Binary search on rate
<!-- * [Capacity to Ship Packages Within D Days](../capacity_to_ship_packages/PROBLEM.md) — Same pattern -->
