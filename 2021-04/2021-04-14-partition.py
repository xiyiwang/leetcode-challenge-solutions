"""
LeetCode Challenge: Partition List (2021-04-14)

Given the head of a linked list and a value x, partition it 
such that all nodes less than x come before nodes greater 
than or equal to x.

You should preserve the original relative order of the nodes 
in each of the two partitions.

Constraints:
- The number of nodes in the list is in the range [0, 200].
- -100 <= Node.val <= 100
- -200 <= x <= 200
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 2-pointer: O(n) - 36ms (beats 54.68%)
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return None
        
        if head.val < x:
            p1, p2 = head, head.next
            while p2 and p2.val < x:
                p1 = p1.next
                p2 = p2.next
            part = prev = p2
            if not p2: return head
        else: 
            p1, part, prev = None, head, head

        p2 = prev.next
        while p2:
            if p2.val < x:
                prev.next = prev.next.next
                tmp = p2
                p2 = prev.next
                if p1:
                    p1.next = tmp
                    tmp.next = part
                    p1 = tmp
                else:
                    p1 = tmp
                    p1.next = head
                    head = p1
            else: 
                prev = p2
                p2 = p2.next

        return head

    # a cleaner 2-pointer solution (official) - O(n) - 32ms
    def partition2(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        after.next = None
        before.next = after_head.next
        
        return before_head.next
