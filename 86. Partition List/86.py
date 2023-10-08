# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None: return head
        
        dummy_node = ListNode(0, head)
        start = dummy_node

        pointer = dummy_node
        while pointer.next and pointer.next.val < x:
            start = pointer.next
            pointer = pointer.next
        
        end = pointer.next
        pointer = end
        while pointer:
            if pointer.next and pointer.next.val < x:
                temp = pointer.next
                pointer.next = temp.next
                temp.next = end
                start.next = temp
                start = start.next
            else:
                pointer = pointer.next

        return dummy_node.next