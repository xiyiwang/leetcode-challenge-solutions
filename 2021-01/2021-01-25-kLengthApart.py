# LeetCode Challenge: Check If All 1's Are at Least Length K Places Away （01/25/2021)

#   Given an array nums of 0s and 1s and an integer k, return True if all 1's are at 
#   least k places away from each other, otherwise return False.
# 
#   Constraints:
#   * 1 <= nums.length <= 10^5
#   * 0 <= k <= nums.length
#   * nums[i] is 0 or 1

#   Submission Detail:
#   * Runtime: 564 ms (better than 66.89% of python3 submissions)
#   * Memory Usage: 17 MB (better than 64.65% of python3 submissions)

def kLengthApart(nums: [int], k: int) -> bool:
    if k == 0 or not 1 in nums:
        return True
    
    # remove leading 0's if any
    first_one_idx = nums.index(1)
    if first_one_idx != 0:
        nums = nums[first_one_idx:]

    while nums:
        if len(nums) == 1 or not 1 in nums[1:]:
            return True
        next_one_idx = nums[1:].index(1) + 1
        if next_one_idx <= k:
            return False
        sub_arr = nums[:next_one_idx]
        if sub_arr: nums = nums[next_one_idx:]
    return True

# Official Solution 1 - One Pass + Counter:
def kLengthApart1(nums: [int], k: int) -> bool:
    # initialize the counter of zeros to k
    # to pass the first 1 in nums
    count = k

    for num in nums:
        # if the current integer is 1
        if num == 1:
            # check that number of zeros in-between 1s
            # is greater than or equal to k
            if count < k:
                return False
            # reinitialize counter
            count = 0
        # if the current integer is 0
        else:
            # increase the counter
            count += 1
    
    return True

# Official Solution 2 - Bit Manipulation:
def kLengthApart2(nums: [int], k: int) -> bool:
    # convert binary array into int
    x = 0
    for num in nums:
        x = (x << 1) | num
    
    # base case
    if x == 0 or k == 0:
        return True
    
    # remove trailing zeros
    while x & 1 == 0:
        x = x >> 1
    
    while x != 1:
        # remove trailing 1-bit
        x = x >> 1
        
        # count trailing zeros
        count = 0
        while x & 1 == 0:
            x = x >> 1
            count += 1
            
        # number of zeros in-between 1-bits
        # should be greater than or equal to k
        if count < k:
            return False
    
    return True
