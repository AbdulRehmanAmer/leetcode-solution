class Solution:
    def jump(self, nums: List[int]) -> int:
        start = end = max_distance = 0
        jump = 0
        
        while start < len(nums) - 1 and end != len(nums):
            max_distance = max(max_distance, start + nums[start])
            if start == end:
                jump += 1
                end = max_distance
            start += 1
        
        return jump