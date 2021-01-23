# LeetCode Challenge: Longest Palindromic Substring (01/19/2021)

def longestPalindrome(s: str) -> str:
    char_set = set(s)
    res = s[0]
    
    # if there're no repeating characters in the string, return the first character
    if len(char_set) == len(s):
        return res

    # if there're repeating characters, find the index of each occurance
    for char in char_set:
        char_count = s.count(char)
        if char_count > 1:
            char_loc = []
            start_index = 0
            for i in range(char_count):
                loc = s.find(char, start_index)
                char_loc.append(loc)
                start_index = loc + 1
            for i in range(len(char_loc)):
                for j in reversed(range(i+1, len(char_loc))):
                    if (char_loc[j] - char_loc[i] + 1) <= len(res):
                        break
                    substring = s[char_loc[i]:(char_loc[j]+1)]
                    if substring == substring[::-1] and len(substring) > len(res):
                        res = substring
    
    return res
    