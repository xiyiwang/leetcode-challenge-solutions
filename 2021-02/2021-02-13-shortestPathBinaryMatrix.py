# LeetCode Challenge: Shortest Path in Binary Matrix (02/13/2021)

#   In an N by N square grid, each cell is either empty (0) 
#   or blocked (1). 
# 
#   A clear path from top-left to bottom-right has length k 
#   if and only if it is composed of cells C_1, C_2, ..., C_k 
#   such that: 
# 
#   * Adjacent cells C_i and C_{i+1} are connected 8-directionally 
#     (ie., they are different and share an edge or corner) 
#   * C_1 is at location (0, 0) (ie. has value grid[0][0]) 
#   * C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1]) 
#   * If C_i is located at (r, c), then grid[r][c] is empty (ie. 
#     grid[r][c] == 0). 
# 
#   Return the length of the shortest such clear path from top-left 
#   to bottom-right.  If such a path does not exist, return -1. 
# 
#   Note: 
#   * 1 <= grid.length == grid[0].length <= 100 
#   * grid[r][c] is 0 or 1

# Solution 1: bfs approach - 736ms
def shortestPathBinaryMatrix(grid): 
    if grid[0][0] != 0: return -1
    
    n = len(grid)
    moves = [[1,-1],[1,1],[-1,-1],[-1,1],[1,0],[0,-1],[0,1],[-1,0]]

    visited = set()
    count = 1

    curr_step = [(0, 0)]
    visited.add((0, 0))
    
    while curr_step:
        next_step = []
        for (x, y) in curr_step:
            if x == y == n-1: return count
            for (dx, dy) in moves:
                if 0<=x+dx<n and 0<=y+dy<n and (x+dx,y+dy) not in visited:
                    if grid[x+dx][y+dy] == 0:
                        next_step.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
        curr_step = next_step
        count += 1

    return -1

# Solution 2: a cleaner bfs approach - 1016ms
def shortestPathBinaryMatrix2(grid): 
    N = len(grid)
    neibs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    queue = [(1, 0, 0)] if grid[0][0] == 0 else []
    visited = set()

    while queue:
        dist, x, y = queue.pop(0)
        if (x, y) == (N-1, N-1): return dist
        for dx, dy in neibs:
            if 0<=x+dx<N and 0<=y+dy<N and grid[x+dx][y+dy] == 0 and (x+dx, y+dy) not in visited:
                visited.add((x+dx, y+dy))
                queue.append((dist+1, x+dx, y+dy))
    
    return -1
