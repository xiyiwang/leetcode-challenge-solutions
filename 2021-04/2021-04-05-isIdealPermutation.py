"""
LeetCode Challenge: Global and Local Inversions (2021-04-05)

We have some permutation A of [0, 1, ..., N - 1], where N is 
the length of A.

The number of (global) inversions is the number of i < j with 
0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 
0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is 
equal to the number of local inversions.

Note:
- A will be a permutation of [0, 1, ..., A.length - 1].
- A will have length in range [1, 5000].
- The time limit for this problem has been reduced.
"""

class Solution:
    # brute force (O(n^2) - exceeds time limit)
    def isIdealPermutation(self, A):
        if len(A) <= 2: return True

        for (i, a) in enumerate(A):
            for b in A[i+2:]:
                if b < a: return False
            
        return True

    # O(n) solution - compare all A[i-1], A[i+1] - 344 ms
    def isIdealPermutation2(self, A):
        level = -1
        for i in range(1, len(A)):
            if A[i] < level: return False
            else: level = max(level, A[i-1])
        return True
