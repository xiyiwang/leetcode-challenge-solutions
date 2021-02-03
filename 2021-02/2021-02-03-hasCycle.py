# LeetCode Challenge: Linked List Cycle (02/03/2021)

#   Given head, the head of a linked list, determine if the 
#   linked list has a cycle in it. 
# 
#   There is a cycle in a linked list if there is some node 
#   in the list that can be reached again by continuously 
#   following the next pointer. Internally, pos is used to 
#   denote the index of the node that tail's next pointer is 
#   connected to. Note that pos is not passed as a parameter. 
# 
#   Return true if there is a cycle in the linked list. Otherwise, 
#   return false. 
# 
#   Constraints: 
#   * The number of the nodes in the list is in the range [0, 10^4]. 
#   * -10^5 <= Node.val <= 10^5 
#   * pos is -1 or a valid index in the linked-list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool: # Time complexity: O(n) - 60ms; Space complexity: O(n) - 17.6MB
    visited = set()
    while head is not None:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False
