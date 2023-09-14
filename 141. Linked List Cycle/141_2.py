# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Through Hashmap
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        objects = dict()
        while head:
            if head in objects:
                return True
            objects[head] = True
            head = head.next
        return False
