import collections
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head):
        nums = collections.deque()
        i = 0
        while head:
            nums.append((i, head.val))
            head = head.next
            i += 1
        
        res = [0] * len(nums)
        stack = list()
        i = 0
        while nums:
            tuple = nums.popleft()
            while stack and tuple[1] > stack[-1][1]:
                res[stack.pop()[0]] = tuple[1]
            
            stack.append(tuple)
            
                
        
        return res
              # For the next greater element we have started from the initial value and have the record of indices in my array. Whenever the greater value found, it pop the values and initialized value at the tracked index in my array, until the increasing interval pattern fulfills.