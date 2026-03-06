# 🎯 Arrays: Two Sum

## 📝 Description
[LeetCode 1](https://leetcode.com/problems/two-sum/)
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## 🚀 Approach 1: Brute Force
Check every pair of numbers to see if they sum up to the target.

### C++ Pseudo-Code
```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[i] + nums[j] == target) return {i, j};
        }
    }
    return {};
}
```

!!! info "Analysis"
    - **Time:** $O(N^2)$ - Nested loops checking all pairs.
    - **Space:** $O(1)$ - No extra data structures.

---

## 🚀 Approach 2: Hash Map (One-Pass) - **Optimal**
As we iterate, store the value and its index in a map. For the current number, check if its "complement" (`target - num`) is already in the map.

### C++ Pseudo-Code
```cpp
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen; // val -> index
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}
```

!!! success "Analysis"
    - **Time:** $O(N)$ - Average time for map insertion and lookup is $O(1)$.
    - **Space:** $O(N)$ - Storing up to $N$ elements in the map.
