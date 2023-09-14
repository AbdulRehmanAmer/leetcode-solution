# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Hare and Tortoise Algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        tortoise = head
        hare = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare: return True


        return False