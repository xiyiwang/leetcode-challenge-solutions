# LeetCode Challenge: Intersection of Two Linked Lists (2021-03-04)

#   Write a program to find the node at which the intersection of 
#   two singly linked lists begins. 
# 
#   Notes: 
#   - If the two linked lists have no intersection at all, return null. 
#   - The linked lists must retain their original structure after the 
#     function returns. 
#   - You may assume there are no cycles anywhere in the entire linked 
#     structure.
#   - Each value on each linked list is in the range [1, 10^9]. 
#   - Your code should preferably run in O(n) time and use only O(1) 
#     memory.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# runtime: 160ms - faster than 76.92%
def getIntersectionNode(headA, headB):
    currA, currB = headA, headB
        
    while currA != currB:
        currB = headA if currB is None else currB.next
        currA = headB if currA is None else currA.next
        
    return currA

