# LeetCode Challenge: Smallest String With A Given Numeric Value (01/28/2021)

#   The numeric value of a lowercase character is defined as its position 
#   (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric 
#   value of b is 2, the numeric value of c is 3, and so on.
#
#   The numeric value of a string consisting of lowercase characters is defined 
#   as the sum of its characters' numeric values. For example, the numeric value 
#   of the string "abe" is equal to 1 + 2 + 5 = 8.
#
#   You are given two integers n and k. Return the lexicographically smallest 
#   string with length equal to n and numeric value equal to k.
#
#   Note that a string x is lexicographically smaller than string y if x comes 
#   before y in dictionary order, that is, either x is a prefix of y, or if i 
#   is the first position such that x[i] != y[i], then x[i] comes before y[i] 
#   in alphabetic order.
#
#   Constraints:
#   * 1 <= n <= 10^5
#   * n <= k <= 26 * n

#   Submission Detail:
#   * Runtime: 40 ms (better than 87.17% of python3 submissions)
#   * Memory Usage: 15.3 MB (better than 82.71% of python3 submissions)

def getSmallestString(n: int, k: int) -> str:
    res = ""

    def intToChar(n: int) -> str:
        return chr(n + 96)

    # ending char != z
    if k - n <= 25:
        if n > 1:
            res += "a" * (n-1)
        res += intToChar(k - n + 1)
    
    # ending char is z
    else:
        # calculate number of ending z's
        z = (k - n) // 25

        if z == n:
            return "z" * z

        # calculate char before z's
        c = intToChar((k - n) % 25 + 1)
        res = "a" * (n - z - 1) + c + "z" * z
        
    return res