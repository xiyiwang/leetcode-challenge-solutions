"""
LeetCode Challenge: Check If a String Contains All Binary Codes of Size K (2021-03-12)

Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s consists of 0's and 1's only.
- 1 <= k <= 20
"""

# Solution 1 - 6008 ms (faster than 10.55%), 18.3 MB (better than 96.2%)
def hasAllCodes(s, k):
    for i in range(2**k):
        if format(i, f'0{k}b') not in s:
            return False
    return True

# Solution 2 - 320 ms (faster than 78.48%), 27 MB
def hasAllCodes2(s, k):
    s_sub = set()
    for i in range(len(s) - k + 1):
        s_sub.add(s[i:i+k])
    return len(s_sub) == 2**k
