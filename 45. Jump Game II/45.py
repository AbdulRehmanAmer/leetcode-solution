class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            jumps[i] = min(jumps[i + 1 : max(nums[i] + i + 1, i + 2)]) + 1

        return jumps[0]