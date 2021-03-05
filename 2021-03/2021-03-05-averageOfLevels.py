# LeetCode Challenge: Average of Levels in Binary Tree (2021-03-05)

#   Given a non-empty binary tree, return the average value of the 
#   nodes on each level in the form of an array. 
# 
#   Note:
#   - The range of node's value is in the range of 32-bit signed 
#     integer.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS approach - 40 ms (faster than 97.89%)
def averageOfLevels(root):
    next_level = [root]
    ans = []
    
    while next_level:
        curr_level = next_level
        next_level = []
        sum = 0
        for node in curr_level:
            sum += node.val
            if node.left:  next_level.append(node.left)
            if node.right: next_level.append(node.right)
        ans.append(sum/len(curr_level))
    
    return ans
