"""
LeetCode Challenge: Determine if String Halves Are Alike (2021-04-07)

You are given a string s of even length. Split this string into two 
halves of equal lengths, and let a be the first half and b be the 
second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 
'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains 
uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Constraints:
- 2 <= s.length <= 1000
- s.length is even.
- s consists of uppercase and lowercase letters.
"""

class Solution:
    # runtime - O(n) - 36 ms (beats 57.17%)
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiou")
        n = len(s)//2
        a, b = s[:n].lower(), s[n:].lower()
        return sum(_ in vowels for _ in a) == sum(_ in vowels for _ in b)
