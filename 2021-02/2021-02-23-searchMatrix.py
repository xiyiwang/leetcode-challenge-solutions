# LeetCode Challenge: Search a 2D Matrix II (2021-02-23)

#   Write an efficient algorithm that searches for a target 
#   value in an m x n integer matrix. The matrix has the 
#   following properties: 
#   * Integers in each row are sorted in ascending from left to right.
#   * Integers in each column are sorted in ascending from top to bottom.
# 
#   Constraints:
#   * m == matrix.length
#   * n == matrix[i].length
#   * 1 <= n, m <= 300
#   * -10^9 <= matix[i][j] <= 10^9
#   * All the integers in each row are sorted in ascending order.
#   * All the integers in each column are sorted in ascending order.
#   * -10^9 <= target <= 10^9

# solution: start with top right corner - 156 ms (faster than 93.65%)
def searchMatrix(matrix, target):
    x, y = len(matrix[0]) - 1, 0
    while x >= 0 and y < len(matrix):
        if matrix[y][x] > target:   x -= 1
        elif matrix[y][x] < target: y += 1
        else:                       return True
    return False
