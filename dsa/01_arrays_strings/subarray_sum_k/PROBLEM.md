# 🎯 Arrays: Subarray Sum Equals K

## 📝 Description
[LeetCode 560](https://leetcode.com/problems/subarray-sum-equals-k/)
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

!!! info "Complexity Analysis"
    - **Time Complexity:** $O(N)$ - We traverse the array once.
    - **Space Complexity:** $O(N)$ - In the worst case, we store all prefix sums in the hash map.

## 🚀 Approach & Intuition
This problem uses the **Prefix Sum** technique combined with a **Hash Map**.
1. We keep track of the cumulative sum (`sum`) as we iterate.
2. If `sum - k` has been seen before, it means the subarray between the previous occurrence and the current index has a sum of `k`.
3. We store the frequency of each prefix sum in a hash map to handle multiple subarrays ending at the same point.

### Key Observations:
- `sum(i, j) = prefix_sum[j] - prefix_sum[i-1]`.
- We want `sum(i, j) = k`, which means `prefix_sum[j] - k = prefix_sum[i-1]`.
- Initializing `mp[0] = 1` handles cases where the subarray starts from the beginning.

## 🛠️ Requirements/Constraints
- $1 <= nums.length <= 2 * 10^4$
- $-1000 <= nums[i] <= 1000$
- $-10^7 <= k <= 10^7$

## 💻 Solution Implementation

```cpp
class Solution {
public:
    int subarraySum(vector<int> &nums, int k) {
        int result = 0;
        int n = nums.size();
        unordered_map<int, int> mp;
        mp[0] = 1; // Base case: prefix sum of 0 seen once
        int current_sum = 0;

        for(int i = 0; i < n; i++) {
            current_sum += nums[i];
            if(mp.find(current_sum - k) != mp.end()) {
                result += mp[current_sum - k];
            }
            mp[current_sum]++;
        }
        return result;
    }
};
```

!!! success "Aha! Moment"
    By transforming the "subarray sum" problem into a "prefix sum difference" problem, we can use a hash map to find solutions in linear time instead of $O(N^2)$.
