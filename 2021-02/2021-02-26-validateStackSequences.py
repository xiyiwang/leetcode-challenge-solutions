# LeetCode Challenge: Validate Stack Sequences (2021-02-26)

#   Given two sequences pushed and popped with distinct values, 
#   return true if and only if this could have been the result 
#   of a sequence of push and pop operations on an initially 
#   empty stack.
# 
#   Constraints:
#   * 0 <= pushed.length == popped.length <= 1000
#   * 0 <= pushed[i], popped[i] < 1000
#   * pushed is a permutation of popped.
#   * pushed and popped have distinct values.

# Stack - 64 ms (faster than 94.09%)
def validateStackSequences(pushed, popped):
    stack = []
    i = 0
    for num in popped:
        if stack and stack[-1] == num: stack.pop()
        elif num in stack: return False
        else:
            while i < len(pushed):
                if pushed[i] == num: 
                    stack.append(pushed[i])
                    stack.pop()
                    i += 1
                    break
                stack.append(pushed[i])
                i += 1
    return True

# Official Solution: Greedy (Same solution, cleaner code) - 64 ms
def validateStackSequences2(pushed, popped):
    pop_count = 0
    stack = []
    for x in pushed:
        stack.append(x)
        while stack and pop_count < len(popped) and stack[-1] == popped[pop_count]:
            stack.pop()
            pop_count += 1
    return pop_count == len(popped)
