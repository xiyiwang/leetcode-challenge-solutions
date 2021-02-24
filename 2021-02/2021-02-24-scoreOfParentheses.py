# LeetCode Challenge: Score of Parentheses (2021-02-24)

#   Given a balanced parentheses string S, compute the 
#   score of the string based on the following rule:
#   * () has score 1
#   * AB has score A + B, where A and B are balanced 
#     parentheses strings.
#   * (A) has score 2 * A, where A is a balanced parentheses 
#     string.
# 
#   Note:
#   1. S is a balanced parentheses string, containing only ( and ).
#   2. 2 <= S.length <= 50

# Stack - 32 ms (faster than 56.58%)
def scoreOfParentheses(S):
    stack = [0] # the score of current frame
    
    for b in S:
        if b == "(": stack.append(0)
        else:
            s = stack.pop()
            stack[-1] += max(2 * s, 1)
    
    return stack.pop()

# Divide & Conquer - 28 ms (faster than 83.5%)
def scoreOfParentheses2(S):
    def F(i, j):
        # score of balanced string S[i:j]
        ans = bal = 0

        # split string into primitives
        for k in range(i, j):
            bal += 1 if S[k] == '(' else -1
            if bal == 0:
                if k - i == 1: ans += 1
                else: ans += 2 * F(i+1, k)
                i = k+1
        
        return ans

    return F(0, len(S))
