"""
LeetCode Challenge: Running Sum of 1d Array (2021-05-03)

Given an array nums. We define a running sum of an array as 
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Constraints:
- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6
"""
class Solution:
    # one-liner solution: 48 ms (beats 18.19%)
    def runningSum(self, nums: list) -> list:
        return [sum(nums[:i+1]) for i in range(len(nums))]
    
    # dp: 40 ms (beats 61.92%)
    def runningSum2(self, nums: list) -> list:
        ans = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] + nums[i]
        return ans
