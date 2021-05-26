"""
LeetCode Challenge: Evaluate Reverse Polish Notation (2021-05-25)

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another 
expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the 
expression would always evaluate to a result, and there will not be any division 
by zero operation.

Constraints:
- 1 <= tokens.length <= 10^4
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the 
  range [-200, 200].
"""

class Solution:
    # stack - O(n)
    def evalRPN(self, tokens: list) -> int:
        def f(op, b, a):
            if op == "+": return a + b
            if op == "-": return a - b
            if op == "*": return a * b
            if op == "/": return int(a / b)
        
        stack = []
        for token in tokens:
            if token in "+-*/":
                stack.append(f(token, stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]

tokens1 = ["2","1","+","3","*"] # 9
tokens2 = ["4","13","5","/","+"] # 6
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # 22
