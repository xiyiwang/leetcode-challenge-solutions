# LeetCode Challenge: Vertical Order Traversal of a Binary Tree (01/29/2021)

#   Given the root of a binary tree, calculate the vertical order traversal 
#   of the binary tree. 
# 
#   For each node at position (x, y), its left and right children will be at 
#   positions (x - 1, y - 1) and (x + 1, y - 1) respectively. 
# 
#   The vertical order traversal of a binary tree is a list of non-empty 
#   reports for each unique x-coordinate from left to right. Each report is 
#   a list of all nodes at a given x-coordinate. The report should be primarily 
#   sorted by y-coordinate from highest y-coordinate to lowest. If any two 
#   nodes have the same y-coordinate in the report, the node with the smaller 
#   value should appear earlier. 
# 
#   Return the vertical order traversal of the binary tree. 
# 
#   Constraints: 
#   * The number of nodes in the tree is in the range [1, 1000] 
#   * 0 <= Node.val <= 1000

#   Submission Detail:
#   * Runtime: 32 ms (better than 80.48% of python3 submissions)
#   * Memory Usage: 14.7 MB (better than 10.11% of python3 submissions)

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        positions = []

        # use dfs to get all the positions
        def dfs(root: TreeNode, x: int, y: int):
            positions.append([x, y, root.val])
            if root.left:
                dfs(root.left, x-1, y-1)
            if root.right:
                dfs(root.right, x+1, y-1)
        
        dfs(root, 0, 0)
        positions.sort(key = lambda a: a[2]) # sort by value
        positions.sort(key = lambda a: a[1], reverse = True) # sort by y
        positions.sort(key = lambda a: a[0]) # sort by x
        
        res = []
        
        left = positions[0][0]
        right = positions[-1][0]
        for i in range(right - left + 1):
            res.append([position[2] for position in positions if position[0] == left + i])
        
        return res
    