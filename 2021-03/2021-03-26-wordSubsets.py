"""
LeetCode Challenge: Word Subsets (2021-03-26)

We are given two arrays A and B of words. Each 
word is a string of lowercase letters.

Now, say that word b is a subset of word a if 
every letter in b occurs in a, including 
multiplicity.  For example, "wrr" is a subset 
of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for 
every b in B, b is a subset of a. 

Return a list of all universal words in A. 
You can return the words in any order.

Note:
- 1 <= A.length, B.length <= 10000
- 1 <= A[i].length, B[i].length <= 10
- A[i] and B[i] consist only of lowercase letters.
- All words in A[i] are unique: there isn't i != j 
  with A[i] == A[j].
"""

# runtime: 876 ms - faster than 55.59%
from collections import Counter
def wordSubsets(A, B):
    BC = Counter()
    for b in B:
        bc = Counter(b)
        for c in bc:
            if bc[c] > BC[c]: BC[c] = bc[c]
    
    ans = []
    for (i, ac) in enumerate([Counter(a) for a in A]):
        if all(BC[char] <= ac[char] for char in BC):
            ans.append(A[i])

    return ans

# Official Solution: Reduce to Single Word in B
# -> same idea, clearer implementation & w/o Counter
# -> slower (1292 ms)
def wordSubsets2(A, B):
    def count(word):
        ans = [0] * 26
        for letter in word:
            ans[ord(letter) - ord("a")] += 1
        return ans
    
    bmax = [0] * 26
    for b in B:
        for i, c in enumerate(count(b)):
            bmax[i] = max(bmax[i], c)

    ans = []
    for a in A:
        if all(x >= y for x, y in zip(count(a), bmax)):
            ans.append(a)
    return ans
    
# Another simple counter solution (1152 ms):
def wordSubsets3(A, B):
    cnt = Counter()
    for b in B:
        cnt |= Counter(b)
    return [a for a in A if not cnt - Counter(a)]
