"""
LeetCode Challenge: Jump Game II (2021-05-05)

Given an array of non-negative integers nums, you are initially 
positioned at the first index of the array.

Each element in the array represents your maximum jump length at 
that position.

Your goal is to reach the last index in the minimum number of 
jumps.

You can assume that you can always reach the last index.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 10^5
"""

from itertools import accumulate

class Solution:
    # dp, backwards - O(N): 28 ms (beats 88.5%)
    def jump(self, nums: list) -> int:
        N = len(nums)
        dp = [float("inf") for _ in range(N)]
        dp[-1] = 0

        for steps_to_goal in range(1, N):
            i = N - steps_to_goal - 1
            max_jump = nums[i]
            if steps_to_goal <= max_jump: dp[i] = 1
            else:
                for n in range(1, max_jump+1):
                    dp[i] = min(dp[i], dp[i+n] + 1)
            
        return dp[0]