class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1: return False
        arr = []
        for i in range(len(nums)):
            if i == len(nums) - 1: return True 
            if not nums[i]:
                while arr and sum(arr[-1]) <= i:
                    arr.pop()
                if not arr: return False
            arr += [ [i, nums[i]] ]