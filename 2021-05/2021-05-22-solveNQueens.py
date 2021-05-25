"""
LeetCode Challenge: N-Queens (2021-05-22)

The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Constraints:
- 1 <= n <= 9
"""
from itertools import product
class Solution:
    # backtrack: O(N!)
    def solveNQueens(self, n: int) -> list:
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board
        
        def backtrack(row, diagonals, anti_diagonals, cols, state):
            if row == n:
                ans.append(create_board(state))
                return

            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                # if the queen is not placeable
                if (col in cols or curr_diagonal in diagonals 
                        or curr_anti_diagonal in anti_diagonals):
                    continue
                
                # add the queen to the board
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                state[row][col] = "Q"

                # move on to the next row with the updated board state
                backtrack(row+1, diagonals, anti_diagonals, cols, state)

                # remove the queen from the board
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                state[row][col] = "."
        
        ans = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return ans

n1 = 4
# output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

n2 = 1
# output: [["Q"]]
