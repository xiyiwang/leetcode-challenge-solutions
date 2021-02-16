# LeetCode Challenge: The K Weakest Rows in a Matrix (02/15/2021)

#   Given a m * n matrix mat of ones (representing soldiers) 
#   and zeros (representing civilians), return the indexes of 
#   the k weakest rows in the matrix ordered from the weakest 
#   to the strongest. 
# 
#   A row i is weaker than row j, if the number of soldiers in 
#   row i is less than the number of soldiers in row j, or they 
#   have the same number of soldiers but i is less than j. 
#   Soldiers are always stand in the frontier of a row, that is, 
#   always ones may appear first and then zeros. 
# 
#   Constraints: 
#   * m == mat.length
#   * n == mat[i].length
#   * 2 <= n, m <= 100 
#   * 1 <= k <= m
#   * matrix[i][j] is either 0 or 1.

# runtime - 108ms
def kWeakestRows(mat, k): 
    m, n = len(mat), len(mat[0])
    strength = []

    for i in range(m):
        count = 0
        for j in range(n):
            if mat[i][j] == 1: count += 1
            else: break
        strength.append((i, count))
    
    strength.sort(key=lambda a:a[1])

    return [s[0] for s in strength[:k]]
