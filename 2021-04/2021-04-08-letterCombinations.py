"""
LeetCode Challenge: Letter Combinations of a Phone Number (2021-04-08)

Given a string containing digits from 2-9 inclusive, return all possible 
letter combinations that the number could represent. Return the answer 
in any order.

A mapping of digit to letters (just like on the telephone buttons) is 
given below. Note that 1 does not map to any letters.
 
Constraints:
- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].
"""

from itertools import product


class Solution:
    # backtrack solution - O(4^n * n)
    def letterCombinations(self, digits):
        if len(digits) == 0: return []
        
        numPad = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
                  "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        def backtrack(i, path):
            if len(path) == len(digits):
                ans.append("".join(path))
                return
              
            cands = numPad[digits[i]]
            for c in cands:
                path.append(c)
                backtrack(i+1, path)
                path.pop()
        
        ans = []
        backtrack(0, [])
        return ans
    
    # use product() - O(4^n * n)
    from itertools import product
    def letterCombinations2(self, digits):
        if not digits: return []
        numPad = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
                  "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        return ["".join(num) for num in product(*[numPad[d] for d in digits])]
