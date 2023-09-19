# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = list()
        start, pointer = head, head
        flag = True
        while True:

            while pointer and len(stack) < k:
                stack.append(pointer.val)
                pointer = pointer.next
            
            if len(stack) == k:
                while start != pointer:
                    start.val = stack.pop()
                    start = start.next
                
            else: break
        
        return head