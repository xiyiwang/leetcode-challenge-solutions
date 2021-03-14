"""
LeetCode Challenge: Swapping Nodes in a Linked List (2021-03-14)

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of 
the kth node from the beginning and the kth node from the end (the 
list is 1-indexed).

Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 10^5
- 0 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime - 1056 ms (faster than 81.75%)
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = 0
        node = head
        while node:
            if n == k-1: l = node
            node = node.next
            n += 1
        
        r = head
        for m in range(n-k):
            r = r.next
        
        l.val, r.val = r.val, l.val
        return head