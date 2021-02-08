# array: easy - Remove Duplicates from Sorted Array

#   Given a sorted array nums, remove the duplicates in-place 
#   such that each element appears only once and returns the 
#   new length. 
# 
#   Do not allocate extra space for another array, you must do 
#   this by modifying the input array in-place with O(1) extra 
#   memory. 
# 
#   Clarification: 
#
#   Confused why the returned value is an integer but your answer 
#   is an array? 
# 
#   Note that the input array is passed in by reference, which 
#   means a modification to the input array will be known to the 
#   caller as well. 
# 
#   Constraints: 
#   * 0 <= nums.length <= 3 * 10^4 
#   * -10^4 <= nums[i] <= 10^4 
#   * nums is sorted in ascending order.


# Solution 1 - 100ms/15.8MB
def removeDuplicates1(nums):
    i = 0
    while i < len(nums) - 1:
        while nums[i] == nums[i + 1]:
            nums.pop(i + 1)
            if i == len(nums) - 1:
                break
        i += 1
    return len(nums)

# Solution 2 (2 pointers) - 80ms/16.1MB
def removeDuplicates2(nums):
    n = len(nums)
    if n <= 1:
        return n
    p1 = 0
    p2 = 1
    while p2 < n:
        if nums[p1] != nums[p2]:
            p1 += 1
            nums[p1] = nums[p2]
        p2 += 1
    return p1 + 1
