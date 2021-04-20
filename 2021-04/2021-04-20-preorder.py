"""
LeetCode Challenge: N-ary Tree Preorder Traversal (2021-04-20)

Given the root of an n-ary tree, return the preorder traversal of 
its nodes' values.

Nary-Tree input serialization is represented in their level order 
traversal. Each group of children is separated by the null value.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- 0 <= Node.val <= 10^4
- The height of the n-ary tree is less than or equal to 1000.
 
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    # dfs: O(N) - 40 ms (beats 98.46%)
    def preorder(self, root: 'Node') -> list:
        def dfs(node):
            if not node: return
            
            ans.append(node.val)
            if node.children:
                for child in node.children:
                    dfs(child)
        
        ans = []
        dfs(root)

        return ans
