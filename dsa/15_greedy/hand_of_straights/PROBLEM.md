#  🃏 Greedy: Hand of Straights

## 📝 Description
[LeetCode 846](https://leetcode.com/problems/hand-of-straights/)
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards. Given an integer array `hand` where `hand[i]` is the value written on the `i`th card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Values represent jumps, costs, or intervals.

## 🧠 The Engineering Story

**The Villain:** "The Random Pick." Picking any card and trying to find its neighbors is inefficient ($O(N^2)$).

**The Hero:** "The Min-Card Starter." A straight *must* start with its smallest card.

**The Plot:**

1. Count frequencies of all cards (TreeMap/Ordered Map or Sorting + HashMap).
2. Start with the smallest card `min_card` in the map.
3. Check if `min_card + 1`, `min_card + 2`... exist.
4. Decrement counts. Remove from map if count becomes 0.
5. Repeat until map is empty.

**The Twist (Failure):** **HashMap vs MinHeap.** Min-Heap is $O(N \log N)$ to pop min. Sorting is also $O(N \log N)$. Both are fine. A generic HashMap ($O(1)$) works if you simply sort unique keys once.

**Interview Signal:** Organizing data to enable **Greedy Choice**.

## 🚀 Approach & Intuition
Always process the smallest available card first.

### C++ Pseudo-Code
```cpp
bool isNStraightHand(vector<int>& hand, int groupSize) {
    if (hand.size() % groupSize != 0) return false;
    map<int, int> count;
    for (int n : hand) count[n]++;
    
    for (auto it = count.begin(); it != count.end(); it++) {
        if (it->second > 0) {
            int start = it->first;
            int freq = it->second;
            // Try to form 'freq' number of straights starting at 'start'
            for (int i = 0; i < groupSize; i++) {
                if (count[start + i] < freq) return false;
                count[start + i] -= freq;
            }
        }
    }
    return true;
}
```

### Key Observations:

- Greedy algorithms make the locally optimal choice at each step with the hope of finding a global optimum.
- The key is to prove that the greedy choice property and optimal substructure hold for the given problem.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log N)$ (Sorting or Heap)
    - **Space Complexity:** $O(N)$

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

- [Merge Triplets](../merge_triplets_to_form_target_triplet/PROBLEM.md) — Next in category
- [Gas Station](../gas_station/PROBLEM.md) — Previous in category
- [Kth Largest in Stream](../../09_heap_priority_queue/kth_largest_element_in_a_stream/PROBLEM.md) — Prerequisite: Heap / Priority Queue
