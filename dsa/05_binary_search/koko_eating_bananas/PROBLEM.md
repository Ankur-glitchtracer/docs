#  🍌 Binary Search: Koko Eating Bananas

## 📝 Description
[LeetCode 875](https://leetcode.com/problems/koko-eating-bananas/)
Koko loves to eat bananas. There are `n` piles of bananas, the `i`th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours. Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour. Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- Target value is within the range of the data type.

## 🧠 The Engineering Story

**The Villain:** "The Simulation." Simulating Koko eating at speed 1, then speed 2, then speed 3... until she finishes in time. If the pile is huge, `k` could be 1 billion. Linear search is dead on arrival.

**The Hero:** "The Binary Search on Answer." We know the answer lies between 1 and `max(piles)`. We can binary search this *range* of possible speeds.

**The Plot:**

1. `low = 1`, `high = max(piles)`.
2. Pick `k = mid`.
3. Calculate hours needed: `sum(ceil(pile / k) for pile in piles)`.
4. If `hours <= h`: This speed works! Try slower (`high = mid - 1`, store `res = mid`).
5. If `hours > h`: Too slow! Need faster (`low = mid + 1`).

**The Twist (Failure):** **Integer Overflow.** The sum of hours can exceed 32-bit integer limits if piles are huge. Use `long long`.

**Interview Signal:** Recognizing **Monotonic Search Spaces**.

## 🚀 Approach & Intuition
Search the range `(To be detailed...)`.

### C++ Pseudo-Code
```cpp
int minEatingSpeed(vector<int>& piles, int h) {
    int l = 1, r = *max_element(piles.begin(), piles.end());
    int res = r;
    
    while (l <= r) {
        int k = l + (r - l) / 2;
        long long hours = 0;
        for (int p : piles) {
            hours += (p + k - 1) / k; // ceil(p/k)
        }
        if (hours <= h) {
            res = k;
            r = k - 1;
        } else {
            l = k + 1;
        }
    }
    return res;
}
```

### Key Observations:

- Binary search can be applied not just to sorted arrays, but to any monotonic search space (Search on Answer).
- Be careful with the boundaries ($left, right$) and the condition for moving them to avoid infinite loops.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N \log(\max(P)))$
    - **Space Complexity:** $O(1)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you apply 'Binary Search on Answer' to solve optimization problems (e.g., minimize max distance)?
- **Scale Question:** If you are searching in a distributed database, how can you reduce the number of network round trips?
- **Edge Case Probe:** Does your mid-point calculation `(left + right) / 2` overflow for very large indices?

## 🔗 Related Problems

- [Find Min in Rotated Array](../find_minimum_in_rotated_sorted_array/PROBLEM.md) — Next in category
- [Search 2D Matrix](../search_2d_matrix/PROBLEM.md) — Previous in category
- [Invert Binary Tree](../../07_trees/invert_binary_tree/PROBLEM.md) — Prerequisite for Trees
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
