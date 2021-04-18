"""
LeetCode Challenge: Number of Submatrices That Sum to Target (2021-04-17)

Given a matrix and a target, return the number of non-empty submatrices 
that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with 
x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different 
if they have some coordinate that is different: for example, if x1 != x1'.

Constraints:
- 1 <= matrix.length <= 100
- 1 <= matrix[0].length <= 100
- -1000 <= matrix[i] <= 1000
- -10^8 <= target <= 10^8
"""

from itertools import accumulate, combinations
from collections import Counter

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        dp, ans = {}, 0
        for k in range(m):
            t = [0] + list(accumulate(matrix[k]))
            for i, j in combinations(range(n+1), 2):
                dp[i, j, k] = dp.get((i,j,k-1), 0) + t[j] - t[i]
        
        for i, j in combinations(range(n+1), 2):
            T = Counter([0])
            for k in range(m):
                ans += T[dp[i, j, k] - target]
                T[dp[i, j, k]] += 1
        
        return ans
