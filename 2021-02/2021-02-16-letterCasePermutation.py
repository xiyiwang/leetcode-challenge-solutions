# LeetCode Challenge: Letter Case Permutation (02/16/2021)

#   Given a string S, we can transform every letter individually 
#   to be lowercase or uppercase to create another string. 
# 
#   Constraints:
#   * S will be a string with length between 1 and 12.
#   * S will consist only of letters or digits.

# Solution 1 - 52 ms
def letterCasePermutation(S):
    ans = []
    for c in S:
        if c.isalpha():
            if not ans:
                ans.append(c.lower())
                ans.append(c.upper())
            else:
                for i in range(len(ans)):
                    ans.append(ans[i]+c.upper())
                    ans[i] += c.lower()
        else:
            if not ans: ans.append(c)
            else: 
                for i in range(len(ans)): ans[i] += c
    return ans

# Solution 2 - dfs - 56ms
def letterCasePermutation2(S):
    def dfs(i, built):
        if i == len(S):
            ans.append(built)
            return
        if S[i].isalpha():
            dfs(i+1, built + S[i].lower())
        dfs(i+1, built + S[i].upper())

    ans = []
    dfs(0, "")
    
    return ans

# Solution 3 - product() - 44 ms
def letterCasePermutation3(S):
    from itertools import product
    return map(''.join, product(*[set([i.lower(), i.upper()]) for i in S]))

S = "a1b2" # ["a1b2","a1B2","A1b2","A1B2"]
# S = "3z4" # ["3z4","3Z4"]
# S = "12345" # ["12345"]
# S = "0" # ["0"]

print(letterCasePermutation3(S))
