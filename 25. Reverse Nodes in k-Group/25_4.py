class Solution:
    def reverseKGroup(self, head, k: int):
        if k == 1: return head
        sentinel_node = ListNode(0, head)
        beforeStart = sentinel_node
        end = head

        i = 1
        while end:

            if i % k == 0:
                start = beforeStart.next
                temp = end.next
                self.reverse_chain(start, end)
                beforeStart.next = end
                start.next = temp

                beforeStart = start
                end = temp

            else:
                end = end.next
            i += 1



        return sentinel_node.next
        

    def reverse_chain(self, start, end):
        print (start, end)
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
        
