# LeetCode Challenge - Roman to Integer (2021-02-20)

#   Given a roman numeral, convert it to an integer. 
# 
#   Constraints:
#   * 1 <= s.length <= 15
#   * s contains only the characters ('I', 'V', 'X', 
#     'L', 'C', 'D', 'M'). 
#   * It is guaranteed that s is a valid roman numeral 
#     in the range [1, 3999].

def romanToInt(s): # 44ms - faster than 83.86%
    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    prev = None
    for c in s:
        if c in ('I', 'X', 'C'):
            if not prev: prev = c
            else:
                if map[prev] < map[c]: 
                    ans += (map[c] - map[prev])
                    prev = None
                else:
                    ans += (map[prev])
                    prev = c
        else:
            ans += map[c]
            if prev:
                if map[prev] < map[c]: ans -= map[prev]
                else:                  ans += map[prev]
            prev = None
    if prev: ans += map[prev]
    return ans

# shorter solution - 40ms
def romanToInt2(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    fix = {'IV': 2, 'IX': 2, 'XL': 20, 'XC': 20, 'CD': 200, 'CM': 200}
    ans = 0
    for elem in s: ans += dic[elem]
    for i, j in zip(s, s[1:]):
        if i + j in fix: ans -= fix[i + j]
    return ans
