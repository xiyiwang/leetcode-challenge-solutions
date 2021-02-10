# LeetCode Challenge: Copy List with Random Pointer (02/10/2021)

#   A linked list of length n is given such that each node contains 
#   an additional random pointer, which could point to any node in 
#   the list, or null. 
# 
#   Construct a deep copy of the list. The deep copy should consist 
#   of exactly n brand new nodes, where each new node has its value 
#   set to the value of its corresponding original node. Both the 
#   next and random pointer of the new nodes should point to new 
#   nodes in the copied list such that the pointers in the original 
#   list and copied list represent the same list state. None of the 
#   pointers in the new list should point to nodes in the original 
#   list. 
# 
#   For example, if there are two nodes X and Y in the original list, 
#   where X.random --> Y, then for the corresponding two nodes x and 
#   y in the copied list, x.random --> y. 
# 
#   Return the head of the copied linked list. 
# 
#   The linked list is represented in the input/output as a list of 
#   n nodes. Each node is represented as a pair of [val, random_index] 
#   where: 
#   * val: an integer representing Node.val 
#   * random_index: the index of the node (range from 0 to n-1) that 
#     the random pointer points to, or null if it does not point to any 
#     node. 
# 
#   Your code will only be given the head of the original linked list. 
# 
#   Constraints: 
#   * 0 <= n <= 1000 
#   * -10000 <= Node.val <= 10000 
#   * Node.random is null or is pointing to some node in the linked list.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Solution 1: Use built-in python deepcopy method - 48ms
def copyRandomList1(head):
    import copy
    return copy.deepcopy(head)

# Solution 2: map out og/copy - 32ms
def copyRandomList2(head):    
    if not head: return None

    _map = dict()
    tmp = Node(-1)
    node = head
    
    while node:
        if node in _map.keys():
            tmp = _map[node]
        else:
            tmp = Node(node.val)
            _map[node] = tmp
        
        if node.next:
            if node.next in _map.keys():
                tmp.next = _map[node.next]
            else:
                tmp.next = Node(node.next.val)
                _map[node.next] = tmp.next
        
        if node.random:
            if node.random in _map.keys():
                tmp.random = _map[node.random]
            else:
                tmp.random = Node(node.random.val)
                _map[node.random] = tmp.random
        
        node = node.next
    
    return _map[head]
