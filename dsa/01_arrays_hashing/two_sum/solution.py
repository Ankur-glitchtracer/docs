def twoSum(nums, target):
    """
    Finds two numbers in nums that add up to target and returns their indices.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    seen = {} # val -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
