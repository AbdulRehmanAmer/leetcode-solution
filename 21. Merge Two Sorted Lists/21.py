# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = ListNode()
        current_pointer = sorted_list
        while list1 or list2:
            n1 = float('inf')
            if list1:
                n1 = list1.val
            n2 = float('inf')
            if list2:
                n2 = list2.val

            if n1 <= n2 and list1:
                current_pointer.next = ListNode(n1)
                current_pointer = current_pointer.next
                list1 = list1.next
            else:
                current_pointer.next = ListNode(n2)
                current_pointer = current_pointer.next
                list2 = list2.next

        return sorted_list.next
                
        