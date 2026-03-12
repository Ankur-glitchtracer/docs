#  ✖️ Arrays & Hashing: Product of Array Except Self

## 📝 Description
[LeetCode 238](https://leetcode.com/problems/product-of-array-except-self/)
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must write an algorithm that runs in $O(N)$ time and without using the division operation.

## 🛠️ Requirements/Constraints

- $2 \le nums.length \le 10^5$
- The product of any prefix or suffix of $nums$ is guaranteed to fit in a 32-bit integer.

## 🧠 The Engineering Story

**The Villain:** "The Forbidden Division." The easiest way is to multiply everything and divide by `nums[i]`. But what if `nums[i]` is zero? Division by zero crashes the system. Also, the problem explicitly bans division.

**The Hero:** "The Prefix & Suffix Multiplier." The product of "everything except `i`" is simply: `(Product of everything to the left) * (Product of everything to the right)`.

**The Plot:**

1. Create a `result` array.
2. **Pass 1 (Prefix):** Store the running product of elements to the *left* in `result`.
3. **Pass 2 (Suffix):** Maintain a running product of elements to the *right* and multiply it with the value already in `result`.

**The Twist (Failure):** **Space Optimization.** A naive solution uses three arrays (prefix, suffix, result). A senior engineer does it in $O(1)$ extra space by using the result array for prefixes and a single variable for the running suffix product.

**Interview Signal:** Mastery of **Prefix/Suffix Operations** without extra storage.

## 🚀 Approach & Intuition
Calculate prefix products in the output array, then multiply by suffix products on the fly.

### C++ Pseudo-Code
```cpp
vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, 1);
    
    // Prefix pass
    int prefix = 1;
    for (int i = 0; i < n; i++) {
        res[i] = prefix;
        prefix *= nums[i];
    }
    
    // Suffix pass
    int suffix = 1;
    for (int i = n - 1; i >= 0; i--) {
        res[i] *= suffix;
        suffix *= nums[i];
    }
    return res;
}
```

### Key Observations:

- By calculating prefix products and suffix products, we can avoid the division operator.
- We can optimize space to $O(1)$ by using the output array to store prefix products and a single variable for suffix products.

!!! info "Complexity Analysis"

    - **Time Complexity:** $O(N)$
    - **Space Complexity:** $O(1)$ (Excluding output array)

## 💻 Solution Implementation

```python
(Implementation details to be added...)
```

!!! success "Aha! Moment"
    (To be detailed...)

## 🎤 Interview Follow-ups

- **Harder Variant:** Can you solve this with $O(1)$ extra space (excluding the output array)?
- **Scale Question:** If the array contains very large numbers that could cause overflow, how would you handle the products?
- **Edge Case Probe:** How does your solution handle a single zero in the array? What about multiple zeros?

## 🔗 Related Problems

- [Valid Sudoku](../valid_sudoku/PROBLEM.md) — Next in category
- [Top K Frequent Elements](../top_k_frequent_elements/PROBLEM.md) — Previous in category
- [Valid Palindrome](../../02_two_pointers/valid_palindrome/PROBLEM.md) — Prerequisite for Two Pointers
- [Valid Parentheses](../../04_stack/valid_parentheses/PROBLEM.md) — Prerequisite for Stack
