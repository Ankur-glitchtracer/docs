#  🪟 Sliding Window: Longest Substring Without Repeating Characters

## 📝 Description
[LeetCode 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
Given a string `s`, find the length of the longest substring without repeating characters.

## 🛠️ Requirements/Constraints

- $0 \le s.length \le 5 \cdot 10^4$
- `s` consists of English letters, digits, symbols and spaces.

## 🧠 The Engineering Story

**The Villain:** "The Redundant Scan." Re-calculating all possible substrings ($O(N^3)$) to find the longest unique one.

**The Hero:** "The Sliding Window." Maintain a window of unique characters and expand/contract it in a single pass ($O(N)$).

**The Plot:**

1. Use a `left` and `right` pointer.
2. Expand `right` and add characters to a set.
3. If a duplicate is found, shrink `left` until the duplicate is gone.
4. Record the max window size at each step.

**The Twist (Failure):** **The Shrinking Invariant.** Forgetting that the left pointer must "jump" efficiently to avoid a secondary loop, or failing to remove characters from the set as the left pointer moves.

**Interview Signal:** Expertise in **Linear Time String Processing** and Windowing techniques.

## 🚀 Approach & Intuition
A sliding window is perfect here because we are looking for a contiguous segment that satisfies a property (uniqueness). As we move the `right` pointer to include new characters, we check if they violate our uniqueness constraint. If they do, we move the `left` pointer to restore the constraint.

### Key Observations:

- A Hash Set is ideal for checking uniqueness in $O(1)$.
- The window size is `right - left + 1`.
- We only need to move the `left` pointer until the current `s[right]` is no longer in the set.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ where $N$ is the length of the string. Each character is visited at most twice (once by each pointer).
    - **Space Complexity:** $O(\min(M, N))$ where $M$ is the size of the character set (e.g., 26 for English letters, 128 for ASCII).

## 💻 Solution Implementation

```python
--8<-- "dsa/03_sliding_window/longest_substring_without_repeating_characters/solution.py"
```

!!! success "Aha! Moment"
    Don't restart the search when you hit a duplicate! Just shrink the "window of opportunity" from the left until the duplicate is gone, then keep moving forward.

## 🎤 Interview Follow-ups

- **Harder Variant:** What if the window size is not fixed, or we need to find the count of all windows satisfying a condition?
- **Scale Question:** In a streaming context (e.g., Flink or Spark Streaming), how would you maintain the window state efficiently?
- **Edge Case Probe:** How do you handle cases where no window satisfies the condition? What about very small inputs?

## 🔗 Related Problems

- [Longest Repeating Replacement](../longest_repeating_character_replacement/PROBLEM.md) — Next in category
- [Best Time to Buy/Sell Stock](../best_time_to_buy_sell_stock/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite: Two Pointers
