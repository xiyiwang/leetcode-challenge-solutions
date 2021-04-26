"""
LeetCode Challenge: Furthest Building You Can Reach (2021-04-26)

You are given an integer array heights representing the heights of 
buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building 
by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),
- If the current building's height is greater than or equal to the next 
  building's height, you do not need a ladder or bricks.
- If the current building's height is less than the next building's height, 
  you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the 
given ladders and bricks optimally.

Constraints:
- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^6
- 0 <= bricks <= 10^9
- 0 <= ladders <= heights.length
"""
from heapq import heappush, heappop

class Solution:
    # binary search - O(n * log n * log n)
    def furthestBuilding(self, heights: list, bricks: int, ladders: int) -> int:
        heights += [float("inf")]
        
        def isReachable(i):
            toClimb = [y - x for x, y in zip(heights[:i], heights[1:]) if y - x > 0]
            return len(toClimb) <= ladders or sum(sorted(toClimb, reverse=True)[ladders:]) <= bricks
        
        beg, end = 0, len(heights)-1
        while beg + 1 < end:
            mid = (beg + end) // 2
            if isReachable(mid): beg = mid
            else: end = mid
        
        return beg
    
    # min-heap - O(N * log N)
    def furthestBuilding2(self, heights: list, bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders > 0:
                    heappush(heap, diff)
                    ladders -= 1
                elif heap and diff > heap[0]:
                    heappush(heap, diff)
                    bricks -= heappop(heap)
                else: bricks -= diff
                if bricks < 0: return i
        
        return len(heights) - 1
        