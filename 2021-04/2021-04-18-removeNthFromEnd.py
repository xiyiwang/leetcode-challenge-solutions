"""
LeetCode Challenge: Remove Nth Node From End of List (2021-04-18)

Given the head of a linked list, remove the nth node from the end 
of the list and return its head.

Follow up: Could you do this in one pass?

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # one-pass: O(n) - 28 ms (beats 91.97%)
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        end = head
        for i in range(n-1):
            end = end.next
        
        if not end.next: return head.next

        N = head
        while end.next:
            end = end.next
            N_prev = N
            N = N.next
        N_prev.next = N.next
        return head.val, head.next.val, head.next.next.val, head.next.next.next.val
