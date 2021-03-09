"""
LeetCode Challenge: Add One Row to Tree (2021-03-09)

Given the root of a binary tree, then value v and depth d, 
you need to add a row of nodes with value v at the given 
depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for 
each NOT null tree nodes N in depth d-1, create two tree 
nodes with value v as N's left subtree root and right 
subtree root. And N's original left subtree should be the 
left subtree of the new left subtree root, its original 
right subtree should be the right subtree of the new right 
subtree root. If depth d is 1 that means there is no depth 
d-1 at all, then create a tree node with value v as the new 
root of the whole original tree, and the original tree is 
the new root's left subtree.

Note:
- The given d is in range [1, maximum depth of the given tree + 1].
- The given binary tree has at least one tree node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# bfs approach - 60 ms (faster than 38.73%)
def addOneRow(root, v, d):
    if d == 1:
        root = TreeNode(val=v, left=root)
        
    else:
        curr_lvl = [root]
        curr_d = 1
        
        while curr_d != d - 1:
            next_lvl = []
            for N in curr_lvl:
                if N.left: next_lvl.append(N.left)
                if N.right: next_lvl.append(N.right)
            curr_lvl = next_lvl
            curr_d += 1
            
        for N in curr_lvl:
            N.left = TreeNode(val=v, left=N.left)
            N.right = TreeNode(val=v, right=N.right)
    
    return root

# dfs approach - 56 ms
def addOneRow(root, v, d):
    def dfs(node, h, dr): # h = height of node, dr = 0 (left child) / 1 (right child)
        if h == d:
            tmp = TreeNode(v)
            # if not node: return tmp
            if dr == 0: tmp.left = node
            else:       tmp.right = node
            return tmp
        
        if not node: return node

        node.left = dfs(node.left, h+1, 0)
        node.right = dfs(node.right, h+1, 1)
        return node
    
    return dfs(root, 1, 0)