"""
LeetCode Challenge: Non-decreasing Array (2021-05-04)

Given an array nums with n integers, your task is to check if 
it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] 
holds for every i (0-based) such that (0 <= i <= n - 2).

Constraints:
- n == nums.length
- 1 <= n <= 10^4
- -10^5 <= nums[i] <= 10^5
"""

class Solution:
    # Find all scenarios: O(N) - 172 ms (beats 96.47%)
    def checkPossibility(self, nums: list) -> bool:
        p, n = -1, len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if p != -1: return False
                p = i
        return p in [-1, 0, n-2] or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]