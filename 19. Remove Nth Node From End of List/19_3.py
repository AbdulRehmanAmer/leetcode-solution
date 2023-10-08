# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy_node = ListNode(0, head)

        p2 = 0
        pointer2 = dummy_node
        while pointer2.next:
            pointer2 = pointer2.next
            p2 += 1
        
        p1 = 0
        pointer1 = dummy_node
        while p2 - p1 != n:
            pointer1 = pointer1.next
            p1 += 1
        pointer1.next = pointer1.next.next
        

        
        return dummy_node.next