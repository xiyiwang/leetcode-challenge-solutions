# LeetCode Challenge: Binary Tree Right Side View (02/06/2021)

#   Given a binary tree, imagine yourself standing on the right 
#   side of it, return the values of the nodes you can see ordered 
#   from top to bottom.

#   Submission Detail:
#   * Runtime: 32 ms (better than 71.24% of python3 submissions)
#   * Memory Usage: 14.2 MB (better than 81.62% of python3 submissions)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    ans = []
    
    if root:
        ans.append(root.val)
        
        current_level = [root]

        while current_level:
            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level
            if next_level: ans.append(next_level[-1].val)
    
    return ans
