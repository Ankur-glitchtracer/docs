#  🔝 Arrays & Hashing: Top K Frequent Elements

## 📝 Description
[LeetCode 347](https://leetcode.com/problems/top-k-frequent-elements/)
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $k$ is in the range $(To be detailed...)$

## 🧠 The Engineering Story

**The Villain:** "The Full Sort." Sorting the entire frequency map ($O(N \log N)$) just to get the top few elements. If $N=10M$ and $K=10$, this is incredibly wasteful.

**The Hero:** "The Bucket Sort (or Heap)." Since frequency cannot exceed the array size $N$, we can use an array of lists (buckets) where index $i$ stores elements that appear $i$ times.

**The Plot:**

1. Count frequencies using a Hash Map ($O(N)$).
2. Create a "Bucket" array where `bucket[i]` contains numbers that appeared `i` times.
3. Iterate backwards from the max frequency.
4. Collect elements until we have $K$ results.

**The Twist (Failure):** **The Min-Heap Alternative.** Using a Min-Heap of size $K$ gives $O(N \log K)$. This is better if the range of frequencies is massive (sparse), but generally Bucket Sort is $O(N)$.

**Interview Signal:** Mastery of **Bucket Sort** and analyzing input constraints.

## 🚀 Approach & Intuition
Count frequencies, then map frequency -> list of numbers.

### C++ Pseudo-Code
```cpp
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> count;
    for (int n : nums) count[n]++;
    
    vector<vector<int>> buckets(nums.size() + 1);
    for (auto p : count) {
        buckets[p.second].push_back(p.first);
    }
    
    vector<int> res;
    for (int i = buckets.size() - 1; i >= 0 && res.size() < k; i--) {
        for (int n : buckets[i]) {
            res.push_back(n);
            if (res.size() == k) return res;
        }
    }
    return res;
}
```

### Key Observations:

- A Max-Heap can solve this in $O(N \log K)$, which is efficient for large $N$ and small $K$.
- Bucket Sort can achieve $O(N)$ time complexity by using the frequency as an index.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ (Bucket Sort) or $O(N \log K)$ (Heap)
    - **Space Complexity:** $O(N)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you achieve $O(N)$ time complexity on average using QuickSelect (Hoare's Selection Algorithm)?
- **Scale Question:** How would you handle this in a real-time system where you need the top $K$ most frequent items in the last hour (Sliding Window)?
- **Edge Case Probe:** What if multiple elements have the same frequency? Does the order of the top $K$ matter?

## 🔗 Related Problems

- [Product of Array Except Self](../product_of_array_except_self/PROBLEM.md) — Next in category
- [Group Anagrams](../group_anagrams/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
