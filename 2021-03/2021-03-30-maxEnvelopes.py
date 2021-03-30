"""
LeetCode Challenge: Russian Doll Envelopes (2021-03-30)

You are given a 2D array of integers envelopes where 
envelopes[i] = [wi, hi] represents the width and the 
height of an envelope.

One envelope can fit into another if and only if both 
the width and height of one envelope is greater than 
the width and height of the other envelope.

Return the maximum number of envelopes can you Russian 
doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Constraints:
- 1 <= envelopes.length <= 5000
- envelopes[i].length == 2
- 1 <= wi, hi <= 10^4
"""
# dp - time complexity: O(N^2)
def maxEnvelopes(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    dp = [1] * len(envelopes)
    
    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][1] > envelopes[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
