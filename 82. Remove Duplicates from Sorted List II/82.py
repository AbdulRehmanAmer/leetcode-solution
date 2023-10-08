class Solution:
    def deleteDuplicates(self, head):
        dummy_node = ListNode(0, head)
        prev = dummy_node

        while head:
            if head.next and head.val == head.next.val:
                duplicate_object = head
                head = head.next
                while head and head.val == duplicate_object.val:
                    head = head.next
                continue

            
            next = head
            
            prev.next = next
            prev = next
            head = head.next
        prev.next = head
        return dummy_node.next