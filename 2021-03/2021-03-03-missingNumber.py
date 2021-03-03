# LeetCode Challenge: Missing Number (2021-03-03)

#   Given an array nums containing n distinct numbers 
#   in the range [0, n], return the only number in the 
#   range that is missing from the array. 
# 
#   Constraints:
#   - n == nums.length
#   - 1 <= n <= 10^4
#   - 0 <= nums[i] <= n
#   - All the numbers of nums are unique.

# runtime - 128 ms (faster than 81.32%)
def missingNumber(nums):
    return list(set(range(0, len(nums) + 1)) - set(nums))[0]

# Official Solution 1: Sorting
# Time complexity: O(nlgn) - 136 ms
# Space complexity: O(1)
def missingNumber2(nums):
    nums.sort()

    # Ensure that n is at the last index
    if nums[-1] != len(nums): return len(nums)

    # Ensure that 0 is at the first index
    if nums[0] != 0: return 0

    # The missing number is in range(0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i-1] + 1
        if nums[i] != expected_num: 
            return expected_num

# Official Solution 2: Hash Set
# Time complexity: O(n) - 132 ms
# Space complexity: O(n)
def missingNumber3(nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            if number not in num_set:
                return number

# Official Solution 3: Bit Manipulation
# Time complexity: O(n) - 128 ms
# Space complexity: O(1)
def missingNumber4(nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing

# Official Solution 4: Gauss' Formula
# Time complexity: O(n) - 128 ms
# Space complexity: O(1)
def missingNumber5(nums):
    expected_sum = len(nums)*(len(nums)+1)//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
