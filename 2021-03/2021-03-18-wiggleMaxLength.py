"""
LeetCode Challenge: Wiggle Subsequence (2021-03-18)

Given an integer array nums, return the length of the 
longest wiggle sequence.

A wiggle sequence is a sequence where the differences 
between successive numbers strictly alternate between 
positive and negative. The first difference (if one exists) 
may be either positive or negative. A sequence with fewer 
than two elements is trivially a wiggle sequence.

- For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence 
  because the differences (6, -3, 5, -7, 3) are alternately 
  positive and negative.
- In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not 
  wiggle sequences, the first because its first two differences 
  are positive and the second because its last difference is 
  zero.

A subsequence is obtained by deleting some elements (eventually, 
also zero) from the original sequence, leaving the remaining 
elements in their original order.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000

Follow up: Could you solve this in O(n) time?
"""
# linear dp - runtime: 28 ms (faster than 94.57%)
def wiggleMaxLength(nums):
    ans = 1
    if len(nums) == 1: return ans

    sign_prev = 0 if nums[1] == nums[0] else (nums[0]-nums[1])//abs(nums[0]-nums[1])

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: continue

        sign = 1 if nums[i] > nums[i-1] else -1
        if sign != sign_prev: 
            ans += 1
            sign_prev = sign
    
    return ans
