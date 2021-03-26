"""
LeetCode Challenge: Pacific Atlantic Water Flow (2021-03-25)

Given an m x n matrix of non-negative integers representing 
the height of each unit cell in a continent, the "Pacific 
ocean" touches the left and top edges of the matrix and the 
"Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or 
right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both 
the Pacific and Atlantic ocean.

Note:
- The order of returned grid coordinates does not matter.
- Both m and n are less than 150.
"""

# Below is a working dfs solution, but pretty slow.
# Would be much easier if the output coords are tuples
# instead of arrays - this makes more sense, and we
# can utilize hashsets to make the search process much
# quicker.

def pacificAtlantic(matrix):
    if not matrix: return []

    m, n = len(matrix), len(matrix[0])
    flowDirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    toPacific = list({(0, y) for y in range(n)} | {(x, 0) for x in range(m)})
    toAtlantic = list({(m-1, y) for y in range(n)} | {(x, n-1) for x in range(m)})

    def dfs(coord, visited):
        (x, y) = coord
        for (dx, dy) in flowDirs:
            if 0<=x+dx<m and 0<=y+dy<n and matrix[x+dx][y+dy]>=matrix[x][y] and (x+dx, y+dy) not in visited:
                visited.append((x+dx, y+dy))
                dfs((x+dx, y+dy), visited)
    
    for (x, y) in toPacific: dfs((x, y), toPacific)
    for (x, y) in toAtlantic: dfs((x, y), toAtlantic)

    ans = list(set(toPacific).intersection(set(toAtlantic)))

    return [list(ans[i]) for i in range(len(ans))]
