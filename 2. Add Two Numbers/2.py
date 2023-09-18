# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        res = ListNode()
        head = res
        carry = 0
        while l1 and l2:
            sum = l1.val + l2.val + carry
            total = sum % 10
            res.next = ListNode(total)
            res = res.next
            carry = sum // 10
            l1 = l1.next
            l2 = l2.next
        return head.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

sol = Solution()
res = sol.addTwoNumbers(l1, l2)
print (res)
