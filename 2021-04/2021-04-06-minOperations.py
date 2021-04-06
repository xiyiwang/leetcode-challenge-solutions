"""
LeetCode Challenge: Minimum Operations to Make Array Equal (2021-04-06)

You have an array arr of length n where arr[i] = (2 * i) + 1 for all 
valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n 
and subtract 1 from arr[x] and add 1 to arr[y] (i.e. perform arr[x] -=1 
and arr[y] += 1). The goal is to make all the elements of the array equal. 
It is guaranteed that all the elements of the array can be made equal using 
some operations.

Given an integer n, the length of the array. Return the minimum number of 
operations needed to make all the elements of arr equal.

Constraints:
- 1 <= n <= 10^4
"""

class Solution:
    # runtime: O(1) - 28 ms - beats 91.63%
    def minOperations(self, n: int) -> int:
        k = n // 2
        return k+k**2 if n%2 else k**2
    
    # one-liner
    def minOperations2(self, n: int) -> int:
        return n**2//4