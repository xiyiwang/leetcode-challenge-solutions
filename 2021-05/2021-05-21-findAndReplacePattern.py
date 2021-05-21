"""
LeetCode Challenge: Find and Replace Pattern (2021-05-21)

Given a list of strings words and a string pattern, return a list of words[i] 
that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that 
after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: 
every letter maps to another letter, and no two letters map to the same letter.

Constraints:
- 1 <= pattern.length <= 20
- 1 <= words.length <= 50
- words[i].length == pattern.length
- pattern and words[i] are lowercase English letters.
"""

class Solution:
    # 2 map solution - runtime: 24 ms (beats 97.69%)
    def findAndReplacePattern(self, words: list, pattern: str) -> list:
        def isPattern(word):
            d1, d2 = dict(), dict()
            for (l1, l2) in zip(word, pattern):
                if l1 not in d1: d1[l1] = l2
                if l2 not in d2: d2[l2] = l1
                if d1[l1] != l2 or d2[l2] != l1: return False
            return True

        return [word for word in words if isPattern(word)]

words1 = ["abc","deq","mee","aqq","dkd","ccc"]
pattern1 = "abb"
# output: ["mee","aqq"]

words2 = ["a","b","c"]
pattern2 = "a"
# output: ["a","b","c"]
