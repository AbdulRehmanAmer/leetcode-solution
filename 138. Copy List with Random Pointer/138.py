"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        temp_hashmap = dict()
        pointer = head
        i = 0
        while pointer:
            temp_hashmap[pointer] = i
            pointer = pointer.next
            i += 1
        temp_hashmap[None] = i

        hashmap = dict() # To store the random pointers
        pointer = head
        while pointer:
            hashmap[pointer] = temp_hashmap[pointer.random]
            pointer = pointer.next

        del temp_hashmap
        
        copied_list = Node(0)
        copy_pointer = copied_list
        copy_hashmap = dict()
        original_pointer = head
        i = 0
        while original_pointer:
            copy_pointer.val = original_pointer.val
            if original_pointer.next:
                copy_pointer.next = Node(original_pointer.next.val)
            else:
                copy_pointer.next = None
            copy_hashmap[i] = copy_pointer

            copy_pointer = copy_pointer.next
            original_pointer = original_pointer.next
            i += 1

        copy_hashmap[i] = None
        copy_pointer = None

        copy_pointer = copied_list
        original_pointer = head
        while original_pointer:
            copy_pointer.random = copy_hashmap[hashmap[original_pointer]]

            copy_pointer = copy_pointer.next
            original_pointer = original_pointer.next


        return copied_list