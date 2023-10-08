# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return head
        n = self.length(head)
        x = n - (k % n)

        if x == 0 or x == n: return head

        pointer = head
        i = 1
        while pointer.next:
            if i == x:
                print (pointer.val)
                temp = pointer.next
                pointer.next = None
                pointer = temp
                i += 1
                continue;
            i += 1
            pointer = pointer.next
        
        pointer.next = head
        return temp


        



    def length(self, head, length = 0):
        while head:
            length += 1
            head = head.next
        return length