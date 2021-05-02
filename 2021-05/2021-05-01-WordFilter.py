"""
LeetCode Challenge: Prefix and Suffix Search (2021-05-01)

Design a special dictionary which has some words and allows you to 
search the words in it by a prefix and a suffix.

Implement the WordFilter class:
- WordFilter(string[] words) Initializes the object with the words in 
  the dictionary.
- f(string prefix, string suffix) Returns the index of the word in the 
  dictionary which has the prefix prefix and the suffix suffix. If there 
  is more than one valid index, return the largest of them. If there is 
  no such word in the dictionary, return -1.

Constraints:
- 1 <= words.length <= 15000
- 1 <= words[i].length <= 10
- 1 <= prefix.length, suffix.length <= 10
- words[i], prefix and suffix consist of lower-case English letters only.
- At most 15000 calls will be made to the function f.
"""

class WordFilter:
    def __init__(self, words: list):
        self.words = words[::-1]
        self.words_rev = [word[::-1] for word in self.words]
        self.k = len(words) - 1
        self.cache = dict()

    def f(self, prefix: str, suffix: str) -> int:
        if (prefix, suffix) in self.cache: return self.cache[(prefix, suffix)]

        for i, word in enumerate(self.words):
            if word.find(prefix) == 0:
                if self.words_rev[i].find(suffix[::-1]) == 0:
                    self.cache[(prefix, suffix)] = self.k - i
                    return self.k - i
        
        self.cache[(prefix, suffix)] = -1
        return -1