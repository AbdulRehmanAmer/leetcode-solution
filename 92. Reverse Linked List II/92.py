class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if right - left == 0: return head

        i = 0
        start, left_node, right_node = head, head, head
        pointer = head
        i = 1
        while i <= right:
            if i == left:
                left_node = pointer
            if i == right:
                right_node = pointer
            if i < left:
                start = pointer
            i += 1
            pointer = pointer.next

        is_matched = False
        if start == left_node:
            is_matched = True
            temp = ListNode(left_node.val)
            temp.next = start
            start = temp

        start.next = right_node.next
        right_node.next = None
        prev, curr, frwd = left_node, left_node.next, left_node.next.next
        for _ in range(left, right):
            curr.next = prev
            if _ == left:
                prev.next = None
            prev = curr
            curr = frwd
            if frwd and frwd.next: frwd = frwd.next 

        end = start.next
        start.next = prev
        left_node.next = end

        if is_matched:
            return start.next

        return head