# 🪜 DP: Climbing Stairs

## 📝 Description
[LeetCode 70](https://leetcode.com/problems/climbing-stairs/)
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## 🚀 Approach 1: Top-Down DP (Memoization)
We can reach step `i` from either step `i-1` or `i-2`. Thus, `ways(i) = ways(i-1) + ways(i-2)`.

### C++ Pseudo-Code
```cpp
int memo[1000]; // Initialize with -1

int climb(int n) {
    if (n <= 1) return 1;
    if (memo[n] != -1) return memo[n];
    
    return memo[n] = climb(n-1) + climb(n-2);
}
```

!!! success "Analysis"
    - **Time:** $O(N)$ - We calculate each state once.
    - **Space:** $O(N)$ - Recursion stack + memo array.

---

## 🚀 Approach 2: Bottom-Up DP (Tabulation) - **Optimal Space**
We don't need the full array. We only need the previous two values to calculate the current one (like Fibonacci).

### C++ Pseudo-Code
```cpp
int climbStairs(int n) {
    if (n <= 1) return 1;
    int prev2 = 1; // Step 0
    int prev1 = 1; // Step 1
    
    for (int i = 2; i <= n; i++) {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}
```

!!! success "Analysis"
    - **Time:** $O(N)$
    - **Space:** $O(1)$ - We optimized away the array!
