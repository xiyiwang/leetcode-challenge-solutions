"""
LeetCode Challenge: Binary Trees With Factors (2021-03-13)

Given an array of unique integers, arr, where each integer 
arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number 
may be used for any number of times. Each non-leaf node's 
value should be equal to the product of the values of its 
children.

Return the number of binary trees we can make. The answer 
may be too large so return the answer modulo 10^9 + 7.

Constraints:
- 1 <= arr.length <= 1000
- 2 <= arr[i] <= 10^9
"""

# runtime - 540 ms (faster than 46.09%)
def numFactoredBinaryTrees(arr):
    dp = dict()
    for num in arr: dp[num] = 1
    
    s_arr = set(arr)

    for num in sorted(arr): 
        for n in arr:
            if num % n == 0 and num//n in s_arr:
                dp[num] += dp[n] * dp[num//n]

    print(dp)
    return sum(dp.values()) % 1000000007
