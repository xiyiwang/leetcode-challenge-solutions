# LeetCode Challenge: Minimize Deviation in Array (01/30/2021)

#   You are given an array nums of n positive integers.
#   
#   You can perform two types of operations on any element of 
#   the array any number of times:
#   * If the element is even, divide it by 2.
#   * If the element is odd, multiply it by 2. 
#   
#   The deviation of the array is the maximum difference between 
#   any two elements in the array. 
# 
#   Return the minimum deviation the array can have after performing 
#   some number of operations. 
# 
#   Constraints:
#   * n == nums.length 
#   * 2 <= n <= 10^5 
#   * 1 <= nums[i] <= 10^9

#   Submission Detail:
#   * Runtime: 1016 ms (better than 45.71% of python3 submissions)
#   * Memory Usage: 30.4 MB (better than 33.59% of python3 submissions)

import heapq

def minimumDeviation(nums: [int]) -> int:
    heap = []
    for num in nums:
        tmp = num
        while tmp % 2 == 0: tmp //= 2
        heap.append((tmp, max(num, tmp*2)))

    _max = max(i for i, j in heap)
    heapq.heapify(heap)
    res = float('inf')
    
    while len(heap) == len(nums):
        num, limit = heapq.heappop(heap)
        res = min(res, _max - num)
        if num < limit:
            heapq.heappush(heap, (num*2, limit))
            _max = max(_max, num*2)
    
    return res
