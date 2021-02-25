# LeetCode Challenge: Shortest Unsorted Continuous Subarray (2021-02-25)

#   Given an integer array nums, you need to find one continuous subarray 
#   that if you only sort this subarray in ascending order, then the whole 
#   array will be sorted in ascending order. 
# 
#   Return the shortest such subarray and output its length.
# 
#   Constraints:
#   * 1 <= nums.length <= 10^4
#   * -10^5 <= nums[i] <= 10^5 

# 188 ms - faster than 94.34%
def findUnsortedSubarray(nums):
    _sorted = sorted(nums)
    if _sorted == nums: return 0

    unsorted = [i for (i, v) in enumerate(nums) if v != _sorted[i]]
    return unsorted[-1] - unsorted[0] + 1
