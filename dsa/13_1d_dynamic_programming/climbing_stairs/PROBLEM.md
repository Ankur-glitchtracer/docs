#  🪜 DP: Climbing Stairs

## 📝 Description
[LeetCode 70](https://leetcode.com/problems/climbing-stairs/)
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## 🛠️ Requirements/Constraints

- $1 <= n <= 45$

## 🧠 The Engineering Story

**The Villain:** "The Exponential Explosion." Solving the problem with simple recursion ($O(2^N)$), where calculating the 50th step takes years of CPU time due to redundant work.

**The Hero:** "The Memoization/Tabulation." Storing the results of smaller sub-problems to build the final answer in $O(N)$ time.

**The Plot:**

1. Realize that to reach step `N`, you must have come from `N-1` or `N-2`.
2. $F(N) = F(N-1) + F(N-2)$.
3. Use an array (Bottom-Up) or a Hash Map (Top-Down) to store seen steps.

**The Twist (Failure):** **The Integer Overflow.** For large `N` (e.g., $N=100$), the number of ways exceeds the capacity of a 64-bit integer.

**Interview Signal:** Mastery of **Sub-problem Decomposition** and **Space Optimization** ($O(1)$ space variant).

## 🚀 Approach & Intuition
This is a classic Dynamic Programming problem that maps directly to the Fibonacci sequence. To reach the $n$-th step, you could have come from either the $(n-1)$-th step (by taking 1 step) or the $(n-2)$-th step (by taking 2 steps). Thus, the total ways to reach $n$ is the sum of ways to reach $n-1$ and $n-2$.

### Key Observations:

- The base cases are: 1 way to reach step 1, 2 ways to reach step 2.
- The recurrence relation is `dp[i] = dp[i-1] + dp[i-2]`.
- We only need the last two results, allowing us to optimize space from $O(N)$ to $O(1)$.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$ - Each step from 1 to $N$ is calculated once.
    - **Space Complexity:** $O(1)$ - We only track the previous two values.

## 💻 Solution Implementation

```python
--8<-- "dsa/13_1d_dynamic_programming/climbing_stairs/solution.py"
```

!!! success "Aha! Moment"
    The realization that "reaching step $N$" depends solely on the steps immediately preceding it transforms an exponential recursive problem into a linear iterative one.

## 🎤 Interview Follow-ups

- **Harder Variant:** What if you can take up to $K$ steps at a time? What if some stairs are 'broken' and cannot be stepped on?
- **Scale Question:** Can you solve this in $O(\log N)$ time using Matrix Exponentiation for very large $N$?
- **Edge Case Probe:** What is the maximum $N$ your solution can handle before the number of ways exceeds a 64-bit integer?

## 🔗 Related Problems

- [Min Cost Climbing Stairs](../min_cost_climbing_stairs/PROBLEM.md) — Next in category
- [Unique Paths](../../14_2d_dynamic_programming/unique_paths/PROBLEM.md) — Prerequisite for 2-D Dynamic Programming
- [Single Number](../../18_bit_manipulation/single_number/PROBLEM.md) — Prerequisite for Bit Manipulation
- [Subsets](../../10_backtracking/subsets/PROBLEM.md) — Prerequisite: Backtracking
