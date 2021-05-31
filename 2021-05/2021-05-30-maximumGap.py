"""
LeetCode Challenge: Maximum Gap (2021-05-30)

Given an integer array nums, return the maximum difference between 
two successive elements in its sorted form. If the array contains 
less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear 
extra space.

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^9
"""

class Solution:
    # one-liner: O(NlogN)
    def maximumGap(self, nums: list) -> int:
        return max([y-x for x,y in zip(sorted(nums), sorted(nums)[1:])]) if len(nums) >= 2 else 0
    
    # bucket sort: O(N)
    def maximumGap2(self, nums: list) -> list:
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        
        bucket = [[] for _ in range(n-1)]
        for num in nums:
            i = n - 2 if num == hi else (num - lo) * (n - 1) // (hi - lo)
            bucket[i].append(num)
        
        cands = [[min(bucket[i]), max(bucket[i])] for i in range(n-1) if bucket[i]]
        return max(y[0]-x[1] for x, y in zip(cands, cands[1:]))

nums1 = [3,6,9,1] # 3
nums2 = [10] # 0
