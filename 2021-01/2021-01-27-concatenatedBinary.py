# LeetCode Challenge: Concatenation of Consecutive Binary Numbers (01/27/2021)

#   Given an integer n, return the decimal value of the binary string formed 
#   by concatenating the binary representations of 1 to n in order, modulo 
#   10^9 + 7. 
#
#   Constraints:
#   * 1 <= n <= 10^5

#   Submission Detail:
#   * Runtime: 2496 ms (better than 25.71% of python3 submissions)
#   * Memory Usage: 17 MB (better than 39.37% of python3 submissions)

def concatenatedBinary(n: int) -> int:
    concat_bin = ""
    for x in range(n):
        x_bin = bin(x + 1).replace("0b", "")
        concat_bin += x_bin
    return int(concat_bin, 2)%1000000007
    