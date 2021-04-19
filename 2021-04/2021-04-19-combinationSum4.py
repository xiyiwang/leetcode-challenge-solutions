"""
LeetCode Challenge: Combination Sum IV (2021-04-19)

Given an array of distinct integers nums and a target integer 
target, return the number of possible combinations that add up 
to target.

The answer is guaranteed to fit in a 32-bit integer.

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of nums are unique.
- 1 <= target <= 1000
"""
class Solution:
    # dp - O(n): 36 ms (beats 89.81%)
    def combinationSum4(self, nums: list, target: int) -> int:
        cache = {}
        
        def dp(t):
            if t in cache:
                return cache[t]
            cnt = 0
            for n in nums:
                if t == n: 
                    cnt += 1
                    continue
                elif t >= n: cnt += dp(t-n)
            cache[t] = cnt
            return cnt
        
        return dp(target)
        