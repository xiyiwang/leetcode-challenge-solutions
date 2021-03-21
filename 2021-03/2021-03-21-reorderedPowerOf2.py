"""
LeetCode Challenge: Reordered Power of 2 (2021-03-21)

Starting with a positive integer N, we reorder the digits 
in any order (including the original order) such that the 
leading digit is not zero.

Return true if and only if we can do this in a way such 
that the resulting number is a power of 2.

Note:
1 <= N <= 10^9
"""

# runtime: 36 ms (faster than 54.44%)
def reorderedPowerOf2(N):
    power_of_2 = set(['1'])
    n = 2
    while 2**n <= 10**9:
        power_of_2.add("".join(sorted(str(2**n))))
        n += 1
    return "".join(sorted(str(N))) in power_of_2

# Official Solution 1: Permutations - runtime: 2492 ms
from itertools import permutations
def reorderedPowerOf2_2(N):
    return any(cand[0] != "0" and bin(int("".join(cand))).count("1") == 1 
        for cand in permutations(str(N)))

# Official Solution 2: Counting - runtime: 36 ms
from collections import Counter
def reorderedPowerOf2_3(N):
    count = Counter(str(N))
    return any(count == Counter(str(1<<b)) for b in range(31))

# N = 1 # True
# N = 10 # False
# N = 16 # True
N = 24 # False
# N = 46 # True

print(reorderedPowerOf2_3(N))
