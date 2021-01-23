# LeetCode Challenge: Sort the Matrix Diagonally （01/23/2021)

#   A matrix diagonal is a diagonal line of cells starting from some 
#   cell in either the topmost row or leftmost column and going in the 
#   bottom-right direction until reaching the matrix's end. 
#   For example, the matrix diagonal starting from mat[2][0], where mat 
#   is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
# 
#   Given an m x n matrix mat of integers, sort each matrix diagonal in 
#   ascending order and return the resulting matrix.
#
#   Constraints:
#   * m == mat.length
#   * n == mat[i].length
#   * 1 <= m, n <= 100
#   * 1 <= mat[i][j] <= 100

# Submission Detail:
# * Runtime: 80 ms (better than 89.62% of python3 submissions)
# * Memory Usage: 14.6 MB (better than 49.8% of python3 submissions)

def diagonalSort(mat):
    m = len(mat)
    n = len(mat[0])
    mat_sorted = mat
    
    # sort top-right half of matrix
    for j in reversed(range(n)):
        j_fix = j
        diag_arr = []
        i = 0
        while n - j != 0 and m - i != 0:
            diag_arr.append(mat[i][j])
            if n - j == 1 or m - i == 1:
                break
            i += 1
            j += 1
        diag_arr.sort()
        for x in range(len(diag_arr)):
            y = j_fix + x
            mat_sorted[x][y] = diag_arr[x]

    # sort bottom-left half of matrix
    for i in reversed(range(1, m)):
        i_fix = i # 2
        diag_arr = []
        j = 0
        while n - j != 0 and m - i != 0:
            diag_arr.append(mat[i][j])
            if n - j == 1 or m - i == 1:
                break
            i += 1
            j += 1
        diag_arr.sort()
        for y in range(len(diag_arr)):
            x = i_fix + y
            mat_sorted[x][y] = diag_arr[y]

    return mat_sorted
