# LeetCode Challenge: Longest Word in Dictionary through Deleting (2021-02-22)

#   Given a string and a string dictionary, find the longest string in 
#   the dictionary that can be formed by deleting some characters of the 
#   given string. If there are more than one possible results, return the 
#   longest word with the smallest lexicographical order. If there is no 
#   possible result, return the empty string. 
# 
#   Note:
#   1. All the strings in the input will only contain lower-case letters.
#   2. The size of the dictionary won't exceed 1,000.
#   3. The length of all the strings in the input won't exceed 1,000.

def findLongestWord(s, d): # 224 ms - faster than 75.62%
    d.sort()
    d.sort(key=len, reverse=True)

    for word in d:
        i = 0
        for char in s:
            if char == word[i]:
                if i == len(word) - 1: return word
                i += 1
    return ""
