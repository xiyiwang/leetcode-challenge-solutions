# LeetCode Challenge: Valid Anagram (02/11/2021)

#   Given two strings s and t , write a function to 
#   determine if t is an anagram of s. 
# 
#   Note: You may assume the string contains only lowercase 
#   alphabets. 
# 
#   Follow up: What if the inputs contain unicode characters? 
#   How would you adapt your solution to such case?

def isAnagram(s: str, t: str) -> bool: # Runtime: 48 ms
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    if s == t:
        return True
    else:
        return False
