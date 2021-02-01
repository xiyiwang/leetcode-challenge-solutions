# LeetCode Challenge: Number of 1 Bits (02/01/2021)

#   Write a function that takes an unsigned integer and 
#   returns the number of '1' bits it has (also known as 
#   the Hamming weight). 
#   
#   Note: 
#   * Note that in some languages such as Java, there is 
#     no unsigned integer type. In this case, the input 
#     will be given as a signed integer type. It should 
#     not affect your implementation, as the integer's 
#     internal binary representation is the same, whether 
#     it is signed or unsigned. 
#   * In Java, the compiler represents the signed integers 
#     using 2's complement notation. Therefore, in Example 
#     3 above, the input represents the signed integer. -3. 
# 
#   Follow up: If this function is called many times, how 
#   would you optimize it? 
# 
#   Example 1: 
#   Input: n = 00000000000000000000000000001011 
#   Output: 3 
# 
#   Example 2: 
#   Input: n = 00000000000000000000000010000000 
#   Output: 1 
# 
#   Example 3: 
#   Input: n = 11111111111111111111111111111101
#   Output: 31 
# 
#   Constraints: 
#   * The input must be a binary string of length 32

#   Submission Detail:
#   * Runtime: 32 ms (better than 62.92% of python3 submissions)
#   * Memory Usage: 14.1 MB (better than 70.08% of python3 submissions)

def hammingWeight(n: int) -> int:
    return str(bin(n)).count("1")
