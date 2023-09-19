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
            curr.next = kth_node
            prev = curr
            curr = next
            if next and next.next: next = next.next
            else: next = None

            while k > 1:
               

                curr.next = prev

                prev = curr
                curr = next
                if next and next.next: next = next.next
                else: next = None

                k -= 1

            k = self.k

            kth_node = self.get_kth_node(k, curr)
            
            if not kth_node: break

            temp = prev_node.next
            prev_node.next = kth_node
            prev_node = temp

        return sentinel_node.next
        
    def get_kth_node(self, k, start):
        while start and k > 1:
            start = start.next
            k -= 1
        return start