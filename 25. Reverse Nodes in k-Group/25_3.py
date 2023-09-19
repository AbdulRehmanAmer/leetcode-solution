class Solution:
    def reverseKGroup(self, head, k: int):
        if 0 <= k <= 1: return head

        self.k = k
        start, end = head, head
        
        while (end) and k > 1:
            end = end.next
            k -= 1
        if not end:
            return head
        
        temp = self.reverseKGroup(end.next, self.k)
        
        self.reverse_chain(start, end)
        start.next = temp


         
        return end


    def reverse_chain(self, start, end):
        prev = start
        current = start.next
        next = current.next
        prev.next = None

        while prev != end:
            current.next = prev

            prev = current
            current = next
            if next: next = next.next
            else: next = None
        
