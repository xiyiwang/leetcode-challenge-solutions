"""
LeetCode Challenge: Ambiguous Coordinates (2021-05-13)

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". 
Then, we removed all commas, decimal points, and spaces, and ended 
up with the string s.  Return a list of strings representing all 
possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never 
started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", 
or any other number that can be represented with less digits.  Also, 
a decimal point within a number never occurs without at least one 
digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all 
coordinates in the final answer have exactly one space between them 
(occurring after the comma.)

Note:
- 4 <= s.length <= 12.
- s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.
"""
from itertools import product
class Solution:
    def ambiguousCoordinates(self, s: str) -> list:
        def make(frag):
            N = len(frag)
            for d in range(1, N+1):
                left = frag[:d]
                right = frag[d:]
                if ((not left.startswith("0") or left == "0") and (not right.endswith("0"))):
                    yield left + ("." if d != N else "") + right
            
        s = s[1:-1]
        return ["({}, {})".format(*cand) for i in range(1, len(s)) for cand in product(make(s[:i]), make(s[i:]))]
