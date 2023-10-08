# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy_node = ListNode(0, head)

        pointer1, pointer2 = dummy_node, dummy_node
        for _ in range(n):
            pointer2 = pointer2.next
        
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        pointer1.next = pointer1.next.next



        
        return dummy_node.next