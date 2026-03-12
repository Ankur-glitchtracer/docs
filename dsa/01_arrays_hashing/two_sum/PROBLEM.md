#  🎯 Arrays & Hashing: Two Sum

## 📝 Description
[LeetCode 1](https://leetcode.com/problems/two-sum/)
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## 🛠️ Requirements/Constraints

- $2 \le nums.length \le 10^4$
- $-10^9 \le nums[i] \le 10^9$
- $-10^9 \le target \le 10^9$
- Only one valid answer exists.

## 🧠 The Engineering Story

**The Villain:** "The $O(N^2)$ Brute Force." Checking every pair for a sum results in nested loops that crash the server for large datasets.

**The Hero:** "The Hash Map (One-Pass)." Trade space for time by storing "seen" numbers to perform an $O(1)$ lookup for the complement.

**The Plot:**

1. Iterate through the array once.
2. For each number, calculate `complement = target - num`.
3. Check if the complement exists in the Hash Map; if so, return the indices.
4. Otherwise, add the current number and its index to the map.

**The Twist (Failure):** **The Duplicate Catch**. Forgetting that a number cannot be used twice (e.g., target is 10, current number is 5).

**Interview Signal:** Mastery of **Space-Time Tradeoffs** and Hash Map lookups.

## 🚀 Approach & Intuition
The core idea is to use a Hash Map to store numbers we've already seen. As we iterate through the array, we check if the "complement" (the value needed to reach the target) is already in our map. This allows us to find the pair in a single pass.

### Key Observations:

- We can find the required complement in $O(1)$ time using a Hash Map.
- A single pass is sufficient if we store values as we go.
- We must return indices, so the map should store `value -> index`.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ because we traverse the list containing $n$ elements only once. Each lookup in the table costs only $O(1)$ time.
    - **Space Complexity:** $O(N)$ The extra space required depends on the number of items stored in the hash table, which stores at most $n$ elements.

## 💻 Solution Implementation

```python
--8<-- "dsa/01_arrays_hashing/two_sum/solution.py"
```

!!! success "Aha! Moment"
    Instead of searching for the second number, we "remember" what we've seen. The Hash Map acts as a memory that lets us look back in time for the perfect partner to our current number.

## 🎤 Interview Follow-ups

- **Harder Variant:** If the input array is sorted, how can you solve this with $O(1)$ space? (See Two Sum II). Also, how would you find all unique triplets that sum to zero (3Sum)?
- **Scale Question:** If the array is too large to fit in memory (e.g., 100GB), how would you use an external sort or a distributed hash table to find the pair?
- **Edge Case Probe:** How does your solution handle multiple pairs that satisfy the condition? What if no such pair exists?

## 🔗 Related Problems

- [Group Anagrams](../group_anagrams/PROBLEM.md) — Next in category
- [Valid Anagram](../valid_anagram/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
