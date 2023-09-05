class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        for i in range(1, len(nums)):
            answer += [answer[-1] * nums[i - 1]]
        
        prod = 1
        for i in range(len(nums) - 2, -2, -1):
            answer[i + 1] *= prod
            prod *= nums[i + 1]

        return answer