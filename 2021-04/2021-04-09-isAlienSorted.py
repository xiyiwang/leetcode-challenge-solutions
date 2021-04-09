"""
LeetCode Challenge: Verifying an Alien Dictionary (2021-04-09)

In an alien language, surprisingly they also use english lowercase 
letters, but possibly in a different order. The order of the 
alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the 
order of the alphabet, return true if and only if the given words 
are sorted lexicographicaly in this alien language.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""

class Solution:
    # runtime: 40 ms (beats 21.29%)
    def isAlienSorted(self, words: list, order: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        _dict = dict(zip(list(order), list(alphabet)))
        
        translation = [""] * len(words)

        for i, word in enumerate(words):
            translation[i] = "".join([_dict[_] for _ in word])

        return translation == sorted(translation)

    # O(m) solution: Compare adjacent words - 32 ms
    def isAlienSorted2(self, words: list, order: str) -> bool:
        order = {char: i for i, char in enumerate(order)}

        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if order[c1] > order[c2]: return False
                    break
            if w1.startswith(w2) and w1 != w2: return False

        return True
        