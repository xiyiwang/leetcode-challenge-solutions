"""
LeetCode Challenge: Max Area of Island (2021-06-01)

You are given an m x n binary matrix grid. An island is a group 
of 1's (representing land) connected 4-directionally (horizontal 
or vertical.) You may assume all four edges of the grid are 
surrounded by water.

The area of an island is the number of cells with a value 1 in 
the island.

Return the maximum area of an island in grid. If there is no 
island, return 0.

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.
"""

class Solution:
    # dfs - O(m*n)
    def maxAreaOfIsland(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def area(x, y):
            if not (0<=x<m and 0<=y<n and (x, y) not in visited and grid[x][y]):
                return 0
            visited.add((x, y))
            return (1 + area(x+1, y) + area(x-1, y) + area(x, y+1) + area(x, y-1))
        
        return max(area(x, y) for x in range(m) for y in range(n))


grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 6

grid2 = [[0,0,0,0,0,0,0,0]]
# 0