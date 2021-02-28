# LeetCode Challenge: Maximum Frequency Stack (2021-02-28)

#   Implement FreqStack, a class which simulates the operation 
#   of a stack-like data structure. 
# 
#   FreqStack has two functions: 
#   * push(int x), which pushes an integer x onto the stack. 
#   * pop(), which removes and returns the most frequent element 
#     in the stack. 
#     * If there is a tie for most frequent element, the element 
#       closest to the top of the stack is removed and returned. 
# 
#   Note: 
#   * Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9. 
#   * It is guaranteed that FreqStack.pop() won't be called if 
#     the stack has zero elements.
#   * The total number of FreqStack.push calls will not exceed 
#     10000 in a single test case. 
#   * The total number of FreqStack.pop calls will not exceed 
#     10000 in a single test case.
#   * The total number of FreqStack.push and FreqStack.pop calls 
#     will not exceed 150000 across all test cases.

from collections import Counter, defaultdict

# 312 ms - faster than 67.53%
class FreqStack:
    def __init__(self):
        self.stacks = defaultdict(list)
        self.freq = Counter()
        self.maxfreq = 0
        
    def push(self, x: int) -> None:
        freq_x = self.freq[x] + 1
        self.freq[x] = freq_x
        self.maxfreq = max(self.maxfreq, freq_x)
        self.stacks[freq_x].append(x)

    def pop(self) -> int:
        x = self.stacks[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.stacks[self.maxfreq]: self.maxfreq -= 1
        return x
