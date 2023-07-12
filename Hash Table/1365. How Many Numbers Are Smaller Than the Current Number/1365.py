# My LeetCode Submission: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/solutions/3753506/linear-time-solution-solution-python-solution/
from operator import itemgetter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Through Monotonic Stack But no popping any element
        monotonic_stack = list()
        ans = [None] * len(nums)

        nums = list(enumerate(nums))
        nums.sort(key = itemgetter(1))

        monotonic_stack.append((nums[0][1], 0))
        ans[nums[0][0]] = 0
        for i in range(1, len(nums)):
            if nums[i][1] == monotonic_stack[-1][0]: monotonic_stack.append((nums[i][1], monotonic_stack[-1][1]))
            else: monotonic_stack.append((nums[i][1], len(monotonic_stack)))
         
            ans[nums[i][0]] = monotonic_stack[-1][1]

        return ans
    