# LeetCode Challenge: Longest Harmonious Subsequence (02/04/2021)

#   We define a harmonious array as an array where the difference 
#   between its maximum value and its minimum value is exactly 1. 
# 
#   Given an integer array nums, return the length of its longest 
#   harmonious subsequence among all its possible subsequences. 
# 
#   A subsequence of array is a sequence that can be derived from 
#   the array by deleting some or no elements without changing the 
#   order of the remaining elements. 
# 
#   Constraints: 
#   * 1 <= nums.length <= 2 * 10^4 
#   * -10^9 <= nums[i] <= 10^9

#   Submission Detail:
#   * Runtime: 316 ms (better than 53.42% of python3 submissions)
#   * Memory Usage: 16.5 MB

def findLHS(nums):
    counter = dict()
    for n in set(nums):
        counter[n] = 0
    for n in nums:
        counter[n] += 1
    
    ans = 0
    for n in counter.keys():
        if n + 1 in counter.keys():
            ans = max(ans, counter[n] + counter[n + 1])
    
    return ans