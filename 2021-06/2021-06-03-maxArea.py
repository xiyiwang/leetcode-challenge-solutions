"""
LeetCode Challenge: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts (2021-06-03)

Given a rectangular cake with height h and width w, and two arrays of integers 
horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from 
the top of the rectangular cake to the ith horizontal cut and similarly, 
verticalCuts[j] is the distance from the left of the rectangular cake to the 
jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and 
vertical position provided in the arrays horizontalCuts and verticalCuts. Since 
the answer can be a huge number, return this modulo 10^9 + 7.

Constraints:
- 2 <= h, w <= 10^9
- 1 <= horizontalCuts.length < min(h, 10^5)
- 1 <= verticalCuts.length < min(w, 10^5)
- 1 <= horizontalCuts[i] < h
- 1 <= verticalCuts[i] < w
- It is guaranteed that all elements in horizontalCuts are distinct.
- It is guaranteed that all elements in verticalCuts are distinct.
"""

class Solution:
    # 3-liner sorted solution
    def maxArea(self, h: int, w: int, horizontalCuts: list, verticalCuts: list) -> int:
        H = sorted([0] + horizontalCuts + [h])
        V = sorted([0] + verticalCuts + [w])
        return max([y-x for x, y in zip(H, H[1:])]) * max([y-x for x, y in zip(V, V[1:])]) % (10**9+7)
        

h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]
# 4

h = 5
w = 4
horizontalCuts = [3,1]
verticalCuts = [1]
# 6

h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]
# 9
