"""
LeetCode Challenge: Flip Binary Tree To Match Preorder Traversal
(2021-03-29)

You are given the root of a binary tree with n nodes, where 
each node is uniquely assigned a value from 1 to n. You are 
also given a sequence of n values voyage, which is the desired 
pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left 
and right subtrees.

Flip the smallest number of nodes so that the pre-order traversal 
of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return 
the answer in any order. If it is impossible to flip the nodes 
in the tree to make the pre-order traversal match voyage, return 
the list [-1].
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flipMatchVoyage(self, root, voyage):
    self.ans = []
    self.i = 0
    
    def dfs(node):
        if node:
            if node.val != voyage[self.i]:
                self.ans = [-1]
                return
            self.i += 1
            
            if self.i < len(voyage) and node.left and node.left.val != voyage[self.i]:
                self.ans.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
    
    dfs(root)
    if self.ans and self.ans[0] == -1: self.ans = [-1]
    return self.ans