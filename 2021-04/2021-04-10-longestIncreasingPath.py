"""
LeetCode Challenge: Longest Increasing Path in a Matrix (2021-04-10)

Given an m x n integers matrix, return the length of the longest 
increasing path in matrix.

From each cell, you can either move in four directions: left, right, 
up, or down. You may not move diagonally or move outside the boundary 
(i.e., wrap-around is not allowed).

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- 0 <= matrix[i][j] <= 2^31 - 1
"""

from functools import lru_cache
from itertools import product

class Solution:
    # dfs + dp: O(mn) - 440 ms (beats 79.32%)
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        @lru_cache(None)
        def dfs(x, y):
            ans = 1
            for dx, dy in directions:
                if 0 <= x+dx < m and 0 <= y+dy < n and matrix[x+dx][y+dy] > matrix[x][y]:
                    ans = max(ans, dfs(x+dx, y+dy) + 1)
            return ans
        
        return max([dfs(x, y) for x, y in product(range(m), range(n))])
