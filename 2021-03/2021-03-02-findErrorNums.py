# LeetCode Challenge: Set Mismatch (2021-03-02)

#   You have a set of integers s, which originally 
#   contains all the numbers from 1 to n. Unfortunately, 
#   due to some error, one of the numbers in s got 
#   duplicated to another number in the set, which 
#   results in repetition of one number and loss of 
#   another number. 
# 
#   You are given an integer array nums representing 
#   the data status of this set after the error. 
# 
#   Find the number that occurs twice and the number 
#   that is missing and return them in the form of an 
#   array. 
# 
#   Constraints: 
#   - 2 <= nums.length <= 10^4 
#   - 1 <= nums[i] <= 10^4

from collections import Counter

# runtime: 188 ms (faster than 82.2%)
def findErrorNums(nums):
    missing = list(set(range(1,len(nums)+1)) - set(nums))[0]
    duplicate = Counter(nums).most_common(1)[0][0]
    return [duplicate, missing]

# Solution 2 - Use Sorting
# runtime: 212 ms - O(n log n)
def findErrorNums2(nums):
    nums.sort()
    dup, missing = -1, 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            dup = nums[i]
        elif nums[i] > nums[i - 1] + 1:
            missing = nums[i - 1] + 1
    if nums[len(nums) - 1] != len(nums): missing = len(nums)
    return [dup, missing]

nums = [1,2,2,4] # [2,3]
# nums = [1,1] # [1,2]

print(findErrorNums3(nums))
