"""
LeetCode Challenge: Deepest Leaves Sum (2021-04-11)

Given the root of a binary tree, return the sum of 
values of its deepest leaves.

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- 1 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # bfs approach - O(n) - 92 ms (beats 71.10%)
    def deepestLeavesSum(self, root: TreeNode) -> int:
        next_level = [root]
        while next_level:
            ans = 0
            curr_level = next_level[:]
            next_level.clear()
            while curr_level:
                node = curr_level.pop()
                if not (node.left or node.right):
                    ans += node.val
                else:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
        return ans