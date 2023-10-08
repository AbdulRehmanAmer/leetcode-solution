# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy_node = ListNode(0, head)

        def aux(pointer):

            if pointer == None:
                return 1
            
            temp = aux(pointer.next)
            if type(temp) == int:
                if temp == n:
                    return pointer.next
                elif temp < n:
                    return temp + 1
                return temp + 1
            else:
                pointer.next = temp
                return 31
            

        
        aux(dummy_node)
        return dummy_node.next