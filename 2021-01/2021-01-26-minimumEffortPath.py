# LeetCode Challenge: Path With Minimum Effort （01/26/2021)

#   You are a hiker preparing for an upcoming hike. You are given heights, 
#   a 2D array of size rows x columns, where heights[row][col] represents 
#   the height of cell (row, col). You are situated in the top-left cell, 
#   (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) 
#   (i.e., 0-indexed). You can move up, down, left, or right, and you wish to 
#   find a route that requires the minimum effort. 
#
#   A route's effort is the maximum absolute difference in heights between 
#   two consecutive cells of the route. 
# 
#   Return the minimum effort required to travel from the top-left cell to 
#   the bottom-right cell. 
#
#   Constraints: 
#   * rows == heights.length 
#   * columns == heights[i].length
#   * 1 <= rows, columns <= 100 
#   * 1 <= heights[i][j] <= 10^6

def minimumEffortPath(heights: [[int]]) -> int:
    m, n = len(heights), len(heights[0])
    nwse = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    # create depth-first search function to traverse through all cells within the LIMIT
    def dfs(LIMIT, x, y):
        visited.add((x, y))
        for dx, dy in nwse:
            if 0<=dx+x<m and 0<=dy+y<n and (dx+x, dy+y) not in visited:
                if abs(heights[x][y] - heights[dx+x][dy+y]) <= LIMIT:
                    dfs(LIMIT, dx+x, dy+y)

    # use binary search to find the minimum effort
    beg, end = -1, max(max(heights, key=max))
    while beg + 1 < end:
        mid = (beg + end) // 2
        visited = set()
        dfs(mid, 0, 0)
        if (m - 1, n - 1) in visited: # if reach the destination, end = mid
            end = mid
        else: # if can't reach the destiniation, beg = mid
            beg = mid
    
    return end