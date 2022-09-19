"""
Two Sum
https://leetcode.com/problems/two-sum/
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num], i
            else:
                lookup[num] = i

# Time Complexity: O(n)
# Space Complexity: O(1)