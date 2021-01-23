# LeetCode Challenge: Determine if Two Strings Are Close (01/22/2021)

#   Two strings are considered close if you can attain one from the other 
#   using the following operations:
#   1. Swap any two existing characters
#   2. Transform every occurrence of one existing character into another 
#      existing character, and do the same with the other character
#
#   Constraints:
#   * 1 <= word1.length, word2.length <= 10^5
#   * word1 and word2 contain only lowercase English letters

# Submission Detail:
# * Runtime: 100 ms (better than 97.71% of python3 submissions)
# * Memory Usage: 15.3 MB (better than 76.23% of python3 submissions)

def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) == len(word2) and len(set(word1)) == len(set(word2)):
        if set(word1) == set(word2):
            char_count_1 = []
            char_count_2 = []
            for char in set(word1):
                char_count_1.append(word1.count(char))
                char_count_2.append(word2.count(char))
            if sorted(char_count_1) != sorted(char_count_2):
                return False
            return True
    return False
    