"""
LeetCode Challenge: Unique Paths II (2021-04-28)

A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.

Now consider if some obstacles are added to the grids. How many 
unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Constraints:
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1.
"""
from itertools import product

class Solution:
    # runtime: O(mn)
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = int(obstacleGrid[0][0] == 0)
        for i, j in product(range(m), range(n)):
            if obstacleGrid[i][j] == 1: continue
            if i > 0: dp[i][j] += dp[i-1][j]
            if j > 0: dp[i][j] += dp[i][j-1]

        return dp[-1][-1]
