# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        if k == 1: return head
        self.k = k
        kth_node = self.get_kth_node(k, head)
        sentinel_node = ListNode(0, kth_node)
        
        prev_node = head
        prev = sentinel_node
        curr = head
        next = curr.next

        while True:
            kth_node = self.get_kth_node(k + 1, curr)
            if not kth_node: break
            if kth_node:
                print ("Hello",kth_node.val)
            else:
                print ("Hello",kth_node)
                

            curr.next = kth_node
                    
            prev = curr
            curr = next
            if next and next.next: next = next.next
            else: next = None

            print ("2.py", prev.val, curr.val, next.val)
            while k > 1:
                curr.next = prev

                prev = curr
                curr = next
                if next and next.next: next = next.next
                else: next = None

                k -= 1

            k = self.k
            kth_node = self.get_kth_node(k, curr)
            if kth_node:
                print ("kth node for prev:", kth_node.val)
            else:
                print ("kth node for prev:", kth_node)
            
            if not kth_node: break
            temp = prev_node
            prev_node.next = kth_node
            prev_node = temp

        return sentinel_node.next
        
    def get_kth_node(self, k, start):
        while start and k > 1:
            start = start.next
            k -= 1
        return start


n = ListNode(1)
head = n
n.next = ListNode(2)
n = n.next
n.next = ListNode(3)
n = n.next
n.next = ListNode(4)
n = n.next
n.next = ListNode(5)
n = n.next
n.next = ListNode(6)
n = n.next


sol = Solution()
sol.reverseKGroup(head, 3)