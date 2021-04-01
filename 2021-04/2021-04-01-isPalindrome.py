"""
LeetCode Challenge: Palindrome Linked List (2021-04-01)

Given the head of a singly linked list, return true if 
it is a palindrome.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # runtime - 828 ms (beats 22.91%)
    def isPalindrome(self, head: ListNode) -> bool:
        visited = []
        while head:
            visited.append(head.val)
            head = head.next
        return visited == visited[::-1]
    
    # runtime - 796 ms
    def isPalindrome2(self, head: ListNode) -> bool:
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        if fast != None: # number of nodes is odd, move mid to the next node
            slow = slow.next
        
        def reverse(head):
            ans = None
            while head != None:
                next = head.next
                head.next = ans
                ans = head
                head = next
            return ans
        
        head2 = reverse(slow) # slow is mid
        while head2 != None:
            if head.val != head2.val: return False
            head = head.next
            head2 = head2.next
        return True

