"""
LeetCode Challenge: Binary Tree Level Order Traversal (2021-05-20)

Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -1000 <= Node.val <= 1000
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # bfs - runtime: 32 ms (beats 80.06%)
    def levelOrder(self, root: TreeNode) -> list:
        if not root: return []

        ans = []
        queue, values = [root], []

        while queue:
            curr_lvl = queue[:]
            queue.clear()
            while curr_lvl:
                node = curr_lvl.pop(0)
                values.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(values[:])
            values.clear()

        return ans

root1 = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
# [3,9,20,None,None,15,7] -> output: [[3],[9,20],[15,7]]

root2 = TreeNode(val=1) 
# output: [[1]]

root3 = None # output: []
