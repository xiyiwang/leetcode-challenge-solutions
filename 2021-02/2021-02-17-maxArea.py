# LeetCode Challenge: Container With Most Water (02/17/2021)

#   Given n non-negative integers a1, a2, ..., an , where each 
#   represents a point at coordinate (i, ai). n vertical lines 
#   are drawn such that the two endpoints of the line i is at 
#   (i, ai) and (i, 0). Find two lines, which, together with 
#   the x-axis forms a container, such that the container contains 
#   the most water. 
#
#   Notice that you may not slant the container. 
# 
#   Constraints:
#   * n == height.length
#   * 2 <= n <= 3 * 10^4 
#   * 0 <= height[i] <= 3 * 10^4

# solution: 2-pointer - 176 ms
def maxArea(height):
    area, left, right = 0, 0, len(height)-1

    while left < right:
        area = max(area, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]: left += 1
        else: right -= 1

    return area
