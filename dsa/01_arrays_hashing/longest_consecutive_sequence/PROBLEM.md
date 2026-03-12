#  🔗 Arrays & Hashing: Longest Consecutive Sequence

## 📝 Description
[LeetCode 128](https://leetcode.com/problems/longest-consecutive-sequence/)
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in $O(N)$ time.

## 🛠️ Requirements/Constraints

- $0 \le nums.length \le 10^5$
- $-10^9 \le nums[i] \le 10^9$

## 🧠 The Engineering Story

**The Villain:** "The Sorting Trap." Sorting the array puts numbers in order, making it easy to find sequences ($O(N \log N)$). But the requirement is $O(N)$.

**The Hero:** "The Start-of-Sequence Check." Only attempt to count a sequence if you are at the *start* of one.

**The Plot:**

1. Put all numbers in a Hash Set for $O(1)$ lookup.
2. Iterate through the set.
3. For each number `num`, check if `num - 1` exists.
   - If `num - 1` exists, `num` is NOT the start. Skip it.
   - If `num - 1` does NOT exist, `num` IS the start. Start counting `num + 1`, `num + 2`...

**The Twist (Failure):** **The Duplicate Redundancy.** Iterating the array instead of the set can lead to redundant checks if duplicates exist. Always iterate the unique set.

**Interview Signal:** Mastery of **HashSet** for $O(N)$ sequence validation.

## 🚀 Approach & Intuition
Use a set to find sequence starts efficiently.

### C++ Pseudo-Code
```cpp
int longestConsecutive(vector<int>& nums) {
    unordered_set<int> s(nums.begin(), nums.end());
    int longest = 0;
    
    for (int num : s) {
        // Only start counting if 'num' is the beginning of a sequence
        if (!s.count(num - 1)) {
            int currentNum = num;
            int currentStreak = 1;
            
            while (s.count(currentNum + 1)) {
                currentNum += 1;
                currentStreak += 1;
            }
            longest = max(longest, currentStreak);
        }
    }
    return longest;
}
```

### Key Observations:

- A Hash Set allows us to check for the existence of neighbors in $O(1)$ time.
- Only start counting from the beginning of a sequence (i.e., `num - 1` is not in the set) to ensure $O(N)$ complexity.

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

- **Harder Variant:** What if the array is dynamic and elements are added/removed? How would you maintain the longest consecutive sequence length?
- **Scale Question:** If the data is distributed, how can you use Union-Find across different shards to find the global longest sequence?
- **Edge Case Probe:** How does the algorithm perform if the array contains many duplicates or is already sorted?

## 🔗 Related Problems

- [Encode and Decode Strings](../encode_and_decode_strings/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
- [Bubble Sort](../../19_sorting/bubble_sort/PROBLEM.md) — Prerequisite for Sorting
