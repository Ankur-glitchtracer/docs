#  🧩 Greedy: Merge Triplets to Form Target Triplet

## 📝 Description
[LeetCode 1899](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/)
A triplet is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [ai, bi, ci]`, and an integer array `target = [x, y, z]`. You want to obtain `target` as a valid triplet by merging any number of triplets. A merge of triplets `[ai, bi, ci]` and `[aj, bj, cj]` is `(To be detailed...)`. Return `true` if you can obtain the target, otherwise `false`.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Values represent jumps, costs, or intervals.

## 🧠 The Engineering Story

**The Villain:** "The Combinatorial Explosion." Trying subsets of triplets to merge.

**The Hero:** "The Filter."

**The Plot:**

1. Filter out useless triplets.
2. Initialize `res = [0, 0, 0]`.
3. Iterate through remaining triplets. `res[i] = max(res[i], triplet[i])`.
4. If `res == target`, return True.

**The Twist (Failure):** **Partial Match.** You don't need *one* triplet to match the target. You need the *max* of all valid triplets to eventually reach the target.

**Interview Signal:** **Filtering Constraints**.

## 🚀 Approach & Intuition
Ignore triplets that exceed target values.

### C++ Pseudo-Code
```cpp
bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
    bool foundX = false, foundY = false, foundZ = false;
    for (auto& t : triplets) {
        if (t[0] > target[0] || t[1] > target[1] || t[2] > target[2])
            continue;
            
        if (t[0] == target[0]) foundX = true;
        if (t[1] == target[1]) foundY = true;
        if (t[2] == target[2]) foundZ = true;
    }
    return foundX && foundY && foundZ;
}
```

### Key Observations:

- Greedy algorithms make the locally optimal choice at each step with the hope of finding a global optimum.
- The key is to prove that the greedy choice property and optimal substructure hold for the given problem.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the input is sorted or has a limited range? Can you optimize space from $O(N)$ to $O(1)$?
- **Scale Question:** If the dataset is too large to fit in RAM, how would you use external sorting or a distributed hash table?
- **Edge Case Probe:** How does your solution handle duplicates, empty inputs, or extremely large integers?

## 🔗 Related Problems

- [Partition Labels](../partition_labels/PROBLEM.md) — Next in category
- [Hand of Straights](../hand_of_straights/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
