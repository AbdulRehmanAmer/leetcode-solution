from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = deque(nums)
        for _ in range(k):
            
            temp.appendleft(temp.pop())
        nums[ : ] = temp
        