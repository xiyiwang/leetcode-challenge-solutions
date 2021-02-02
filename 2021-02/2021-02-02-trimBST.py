# LeetCode Challenge: Trim a Binary Search Tree (02/02/2021)

#   Given the `root` of a binary search tree and the lowest and 
#   highest boundaries as `low` and `high`, trim the tree so that 
#   all its elements lies in `[low, high]`. Trimming the tree 
#   should not change the relative structure of the elements 
#   that will remain in the tree (i.e., any node's descendant 
#   should remain a descendant). It can be proven that there 
#   is a **unique answer**. 
# 
#   Return *the root of the trimmed binary search tree*. Note that 
#   the root may change depending on the given bounds. 
# 
#   Constraints: 
#   * The number of nodes in the tree in the range [1, 10^4]. 
#   * 0 <= Node.val <= 10^4 
#   * The value of each node in the tree is unique. 
#   * root is guaranteed to be a valid binary search tree. 
#   * 0 <= low <= high <= 10^4

#   Submission Detail:
#   * Runtime: 52 ms (better than 58% of python3 submissions)
#   * Memory Usage: 18.3 MB

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def trimBST(root: TreeNode, low: int, high: int) -> TreeNode:
    def dfs(node):
        if node:
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
    
    return dfs(root)
