# LeetCode Challenge: Broken Calculator (2021-02-21)

#   On a broken calculator that has a number showing on 
#   its display, we can perform two operations: 
#   * Double: Multiply the number on the display by 2, or; 
#   * Decrement: Subtract 1 from the number on the display. 
# 
#   Initially, the calculator is displaying the number X. 
# 
#   Return the minimum number of operations needed to display 
#   the number Y. 
# 
#   Note:
#   * 1 <= X <= 10^9
#   * 1 <= Y <= 10^9

def brokenCalc(X, Y): # 24ms - faster than 96.68%
    ans = 0
    while Y > X:
        if Y % 2: Y += 1
        else:     Y /= 2
        ans += 1
    return int(ans + X - Y)
