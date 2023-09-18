# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = list()
        pointer = head
        for _ in range(left):
            reverse_pointer = pointer
            pointer = pointer.next
        pointer = reverse_pointer
        for _ in range(left, right + 1):
            stack.append(pointer.val)
            pointer = pointer.next
        for _ in range(left, right + 1):
            reverse_pointer.val = stack.pop()
            reverse_pointer = reverse_pointer.next
        
        return head
        

        
        

        