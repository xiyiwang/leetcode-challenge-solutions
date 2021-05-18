"""
LeetCode Challenge: Flatten Binary Tree to Linked List (2021-05-14)

Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right 
  child pointer points to the next node in the list and the left child 
  pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal 
  of the binary tree.

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
- -100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # dfs: runtime - 36 ms (beats 74.13%)
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return

        def dfs(node):
            queue.append(node)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        queue = []
        dfs(root)
        node = TreeNode(val=101) # dummy
        while queue:
            node.left = None
            node.right = queue.pop(0)
            node = node.right