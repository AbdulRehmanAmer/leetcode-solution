# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Monotonic Stack
        stack = collections.deque()

        while head:
            n = head.val
            while stack and n > stack[-1].val:
                stack.pop()
            stack.append(head)
            head = head.next
        
        # Maintaining Connections

        head = stack.popleft()
        cur = head
        while stack:
            cur.next = stack.popleft()
            cur = cur.next
        return head


        # Monotonic Stack is filling in the increasing interval [pattern]. Whenever a value encounters that disrupts the pattern of this data structure stack pop all of it values until the previous larger value does not occur.
        