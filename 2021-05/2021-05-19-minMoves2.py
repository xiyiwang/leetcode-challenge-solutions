"""
LeetCode Challenge: Minimum Moves to Equal Array Elements II (2021-05-19)

Given an integer array nums of size n, return the minimum number of moves 
required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Constraints:
- n == nums.length
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from statistics import median

class Solution:
    # runtime: 72 ms (beats 70.63%)
    def minMoves2(self, nums: list) -> int:
        m = int(median(nums))
        return sum([abs(_ - m) for _ in nums])

nums1 = [1,2,3] # output: 2
nums2 = [1,10,2,9] # output: 16
nums3 = [1,0,0,8,6] # output: 14
