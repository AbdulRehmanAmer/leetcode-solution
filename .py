# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left: int, right: int) :
        if left == right: return head
        sentinel_node = ListNode(0, head)
        pointer = head
        prev = head
        for _ in range(left - 1):
            prev = pointer
            pointer = pointer.next

        start, end, right_node = self.reverse_chain(pointer, left, right)

        start.next = right_node
        
        if left == 1: 
            sentinel_node.next = end
        else:
            prev.next = end

        return sentinel_node.next
        
    def reverse_chain(self, head, left, right):
        start = head
        current_node = head
        right_node = current_node.next
        for i in range(left, right):
            temp = right_node.next
            right_node.next = current_node
            current_node = right_node
            right_node = temp

            if i == right - 1:
                return start, current_node, right_node
        



            





n = ListNode(3)
head = n
n.next = ListNode(5)
n = n.next


sol = Solution()
sol.reverseBetween(head, 1, 2)