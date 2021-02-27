# LeetCode Challenge: Divide Two Integers (2021-02-27)

#   Given two integers dividend and divisor, divide two 
#   integers without using multiplication, division, and 
#   mod operator. 
# 
#   Return the quotient after dividing dividend by divisor. 
# 
#   The integer division should truncate toward zero, which 
#   means losing its fractional part. For example, 
#   truncate(8.345) = 8 and truncate(-2.7335) = -2.
# 
#   Note: 
#   * Assume we are dealing with an environment that could 
#     only store integers within the 32-bit signed integer 
#     range: [−2^31,  2^31 − 1]. For this problem, assume 
#     that your function returns 231 − 1 when the division 
#     result overflows. 
# 
#   Constraints:
#   * -2^31 <= dividend, divisor <= 2^31 - 1
#   * divisor != 0

# runtime - 28 ms (faster than 92.03%)
def divide(dividend, divisor):
    def _divide(ans, d1, d2):
        tmp = 0
        
        while d1 >= d2:
            if tmp == 0: tmp += 1
            else: tmp += tmp

            if d1 > d2 + d2: d2 += d2
            else: break
        
        ans += tmp

        if d1 - d2 > 0:
            return(_divide(ans, d1-d2, abs(divisor)))
        else: return ans

    if (dividend > 0 == divisor > 0):
        ans = min(_divide(0, abs(dividend), abs(divisor)), ((1<<31)-1))
    else:
        ans = max(-(_divide(0, abs(dividend), abs(divisor))), (-1<<31))

    return ans
