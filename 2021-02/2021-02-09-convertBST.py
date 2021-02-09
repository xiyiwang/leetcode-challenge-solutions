# LeetCode Challenge: Convert BST to Greater Tree (02/09/2021)

#   Given the root of a Binary Search Tree (BST), convert it 
#   to a Greater Tree such that every key of the original BST 
#   is changed to the original key plus sum of all keys greater 
#   than the original key in BST. 
# 
#   As a reminder, a binary search tree is a tree that satisfies 
#   these constraints: 
#   * The left subtree of a node contains only nodes with keys 
#     less than the node's key. 
#   * The right subtree of a node contains only nodes with keys 
#     greater than the node's key. 
#   * Both the left and right subtrees must also be binary search 
#     trees. 
# 
#   Constraints: 
#   * The number of nodes in the tree is in the range [0, 10^4]. 
#   * -10^4 <= Node.val <= 10^4 
#   * All the values in the tree are unique. 
#   * root is guaranteed to be a valid binary search tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# an inefficient 2xdfs approach - 540ms
def convertBST1(root):
    if not root: return root
    
    node_vals = []
    _dict = {}
    
    def dfs_get_vals(node):
        node_vals.append(node.val)
        if node.left:  dfs_get_vals(node.left)
        if node.right: dfs_get_vals(node.right)
    
    dfs_get_vals(root)
    node_vals.sort()
    
    for i in range(len(node_vals)):
        _dict[node_vals[i]] = sum(node_vals[i:])
    
    def dfs_set_vals(node):
        node.val = _dict[node.val]
        if node.left:  dfs_set_vals(node.left)
        if node.right: dfs_set_vals(node.right)
    
    dfs_set_vals(root)
    return root

# official solution 1 (recursion) for reverse in-order traversal - 72ms
def convertBST2(root):
    total = 0
    if root is not None:
        convertBST2(root.right)
        total += root.val
        root.val = total
        convertBST2(root.left)
    return root

# official solution 2 (iteration w. stack) - 72ms
def convertBST3(root):
    total = 0
        
    node = root
    stack = []
    
    while stack or node is not None:
        # push all nodes up to (and including) this subtree's maximum 
        # on the stack
        while node is not None:
            stack.append(node)
            node = node.right
        
        node = stack.pop()
        total += node.val
        node.val = total
        
        # all nodes with values between the current and its parent lie 
        # in the left subtree
        node = node.left
    
    return root