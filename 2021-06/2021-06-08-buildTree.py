"""
LeetCode Challenge: Construct Binary Tree from Preorder and Inorder Traversal (2021-06-08)

Given two integer arrays preorder and inorder where preorder is the preorder 
traversal of a binary tree and inorder is the inorder traversal of the same 
tree, construct and return the binary tree.

Constraints:
- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        def helper(l, r):
            nonlocal i
            
            if l > r: return None

            root_val = preorder[i]
            root = TreeNode(root_val)
            i += 1
            
            root.left = helper(l, inorder.index(root_val) - 1)
            root.right = helper(inorder.index(root_val) + 1, r)

            return root
        i = 0
        return helper(0, len(preorder) - 1)