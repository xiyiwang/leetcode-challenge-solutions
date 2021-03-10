"""
LeetCode Challenge: Integer to Roman (2021-03-10)

Given an integer, convert it to a roman numeral.

Constraints:
- 1 <= num <= 3999
"""

# runtime - 44 ms (faster than 87.75%)
def intToRoman(num):
    ans = ""
    num_str = format(num, "04d")
    th, h, t, o = int(num_str[0]), int(num_str[1]), int(num_str[2]), int(num_str[3])
    
    # thousands: 0~3
    ans += "M" * th
    
    # hundreds: 0~9
    if h == 4:   ans += "CD"
    elif h == 9: ans += "CM"
    elif h >= 5:  
        ans += ("D" + "C" * (h - 5))
    else: ans += "C" * h

    # tens: 0~9
    if t == 4:   ans += "XL"
    elif t == 9: ans += "XC"
    elif t >= 5:
        ans += ("L" + "X" * (t - 5))
    else: ans += "X" * t
    
    # ones: 0~9
    if o == 4:   ans += "IV"
    elif o == 9: ans += "IX"
    elif o >= 5:
        ans += ("V" + "I" * (o - 5))
    else: ans += "I" * o

    return ans

# a shorter solution: 56 ms
def intToRoman2(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    ans = ""
    for i in range(len(val)):
        while num >= val[i]:
            ans += rom[i]
            num -= val[i]
    return ans
