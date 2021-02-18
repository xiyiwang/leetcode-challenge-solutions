# LeetCode Challenge: Arithmetic Slices (02/18/2021)

#   A sequence of numbers is called arithmetic if it consists 
#   of at least three elements and if the difference between 
#   any two consecutive elements is the same. 
# 
#   A zero-indexed array A consisting of N numbers is given. 
#   A slice of that array is any pair of integers (P, Q) such 
#   that 0 <= P < Q < N. 
# 
#   A slice (P, Q) of the array A is called arithmetic if the 
#   sequence: A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. 
#   In particular, this means that P + 1 < Q. 
# 
#   The function should return the number of arithmetic slices 
#   in the array A.

# 2-pointer solution: 36 ms
def numberOfArithmeticSlices(A):
    count = 0
    for p1 in range(len(A)-2):
        d = A[p1+1] - A[p1]
        p2 = p1 + 2
        while p2 <= len(A) - 1:
            if (A[p2] - A[p1]) / (p2 - p1) == d: 
                count += 1
                p2 += 1
            else: break
    return count
