#  🚫 Arrays & Hashing: Contains Duplicate

## 📝 Description
[LeetCode 217](https://leetcode.com/problems/contains-duplicate/)
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## 🛠️ Requirements/Constraints

- $1 \le nums.length \le 10^5$
- $-10^9 \le nums[i] \le 10^9$

## 🧠 The Engineering Story

**The Villain:** "The Naive Scan." Checking every element against every other element to find a duplicate ($O(N^2)$). For a database of 1 million users, this will timeout your API.

**The Hero:** "The Hash Set." Trading memory for speed. By storing seen elements in a set, we can check for duplicates in $O(1)$ on average.

**The Plot:**

1. Initialize an empty hash set.
2. Iterate through the array.
3. If the element is already in the set, return `true` (duplicate found).
4. Otherwise, add the element to the set.
5. If the loop finishes, return `false`.

**The Twist (Failure):** **The Memory Limit.** If the dataset is massive (e.g., streaming logs), storing everything in a set might crash the RAM. In that case, sorting ($O(N \log N)$) might be preferred.

**Interview Signal:** Understanding of **Space-Time Tradeoffs**.

## 🚀 Approach & Intuition
Use a hash set to store elements we've seen so far.

### C++ Pseudo-Code
```cpp
bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> seen;
    for (int num : nums) {
        if (seen.count(num)) return true;
        seen.insert(num);
    }
    return false;
}
```

### Key Observations:

- A Hash Set provides $O(1)$ average time complexity for lookups, making it the most efficient way to detect duplicates.
- Sorting the array first ($O(N \log N)$) allows for $O(1)$ extra space if memory is a major constraint.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(N)$

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** What if you are only allowed $O(1)$ extra space? (Hint: sorting). What if you need to find the first duplicate that appears twice?
- **Scale Question:** If the data is a stream, how would you handle a 'sliding window' of the last $K$ elements to check for duplicates?
- **Edge Case Probe:** How does the performance change if the range of numbers is very small (e.g., 1-100) vs very large (e.g., $10^9$)?

## 🔗 Related Problems

- [Valid Anagram](../valid_anagram/PROBLEM.md) — Next in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
- [Bubble Sort](../../19_sorting/bubble_sort/PROBLEM.md) — Prerequisite for Sorting
