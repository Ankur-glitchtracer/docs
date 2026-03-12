# 🧠 DSA Patterns: The Senior Registry

## 🪟 Archetype: Sliding Window

**The Villain:** "The Redundant Scan." Re-calculating sums or counts for a range from scratch every time the start index moves.

**The Hero:** "The Running State." Only updating the state with the *new* element entering the window and the *old* one leaving.

**The Plot:**

1. Expand the `right` pointer to include new data.
2. Once the condition is violated, contract the `left` pointer.
3. Capture the result (max, min, or count) at each valid step.
**🎯 Field Manual (Local Files):**

- [Longest Substring](./03_sliding_window/longest_substring_without_repeating_characters/PROBLEM.md)
- [Sliding Window Maximum](./03_sliding_window/sliding_window_maximum/PROBLEM.md)

## 🏎️ Archetype: Two Pointers (Converging)

**The Villain:** "The $O(N^2)$ Pair Search." Using nested loops to find a pair that meets a condition.

**The Hero:** "The Greedy Squeeze." Starting from both ends and moving inward.
**🎯 Field Manual (Local Files):**

- [Two Sum](./01_arrays_hashing/two_sum/PROBLEM.md)
- [3Sum](./02_two_pointers/3sum/PROBLEM.md)
- [Trapping Rain Water](./02_two_pointers/trapping_rain_water/PROBLEM.md)

## 🐢 Archetype: Fast & Slow Pointers (Tortoise & Hare)

**The Villain:** "The Infinite Loop." Traversing a structure that has a cycle.

**The Hero:** "The Relative Velocity." Two pointers moving at different speeds will eventually meet.
**🎯 Field Manual (Local Files):**

- [Linked List Cycle](./06_linked_list/linked_list_cycle/PROBLEM.md)
- [Palindrome Linked List](./06_linked_list/palindrome_linked_list/PROBLEM.md)

## 🌲 Archetype: Level-Order Traversal (BFS)

**The Villain:** "The Fog of War." Not knowing the shortest path or the "width" of a tree.

**The Hero:** "The FIFO Queue." Processing layer by layer.
**🎯 Field Manual (Local Files):**

- [Level Order Traversal](./07_trees/binary_tree_level_order_traversal/PROBLEM.md)
- [Rotting Oranges](./11_graphs/rotting_oranges/PROBLEM.md)

## 🏗️ Archetype: Depth-First Search (DFS)

**The Villain:** "The Unexplored Path." Needing to visit every node or find all possible combinations.

**The Hero:** "The Stack / Recursion." Diving deep into one path before backtracking.
**🎯 Field Manual (Local Files):**

- [Max Depth](./07_trees/maximum_depth_of_binary_tree/PROBLEM.md)
- [Number of Islands](./11_graphs/number_of_islands/PROBLEM.md)
- [Permutations](./10_backtracking/permutations/PROBLEM.md)

## 🪜 Archetype: Dynamic Programming (Tabulation)

**The Villain:** "The Redundant Recursion." Solving the same sub-problem $2^N$ times.

**The Hero:** "The Cache." Storing results in an array to solve in $O(N)$.
**🎯 Field Manual (Local Files):**

- [Coin Change](./13_1d_dynamic_programming/coin_change/PROBLEM.md)
- [Longest Common Subsequence](./14_2d_dynamic_programming/longest_common_subsequence/PROBLEM.md)

## 🫧 Archetype: Sorting (Divide & Conquer)

**The Villain:** "The $O(N^2)$ Bottleneck." Trying to sort millions of items with Bubble or Insertion sort.

**The Hero:** "The Recursive Splitter." Breaking the problem into single-element arrays and merging them back (Merge Sort) or partitioning around a pivot (Quick Sort).
**🎯 Field Manual (Local Files):**

- [Merge Sort](./19_sorting/merge_sort/PROBLEM.md)
- [Quick Sort](./19_sorting/quick_sort/PROBLEM.md)
