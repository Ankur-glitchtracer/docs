# 🎯 Arrays: Subarrays with XOR K

## 📝 Description
[GeeksForGeeks](https://www.geeksforgeeks.org/count-number-subarrays-given-xor/)
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose XOR sum equals to `k`.

!!! info "Complexity Analysis"
    - **Time Complexity:** $O(N)$ - We traverse the array once.
    - **Space Complexity:** $O(N)$ - We store prefix XOR values in the hash map.

## 🚀 Approach & Intuition
This problem is an XOR variant of the "Subarray Sum Equals K" problem.
1. We use the property of XOR: if `A ^ B = C`, then `A ^ C = B`.
2. We maintain a prefix XOR (`xr`) as we iterate.
3. If `xr ^ k` exists in our map, it means there is a prefix such that `prefix_xor ^ current_xor = k`.
4. We store the frequency of each prefix XOR in a hash map.

### Key Observations:
- `xor(i, j) = prefix_xor[j] ^ prefix_xor[i-1]`.
- We want `prefix_xor[j] ^ prefix_xor[i-1] = k`.
- Rearranging gives: `prefix_xor[j] ^ k = prefix_xor[i-1]`.

## 🛠️ Requirements/Constraints
- $1 <= nums.length <= 10^5$
- $0 <= nums[i], k <= 10^6$

## 💻 Solution Implementation

```cpp
class Solution {
public:
    int subarraysWithXorK(vector<int> &nums, int k) {
        int result = 0;
        int n = nums.size();
        unordered_map<int, int> mp;
        mp[0] = 1; // Base case: prefix XOR of 0 seen once
        int xr = 0;

        for(int i = 0; i < n; i++) {
            xr = xr ^ nums[i];
            // If xr ^ k = some_previous_prefix_xor, then current_sub-array_xor = k
            if(mp.find(xr ^ k) != mp.end()){
                result += mp[xr ^ k];
            }
            mp[xr]++;
        }
        return result;
    }
};
```

!!! success "Aha! Moment"
    The same "Prefix + Hash Map" logic used for sums applies perfectly to XOR because of the self-inverse property of the XOR operation.
