class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = list()
        product = 1
        for x in nums:
            left += [product * x]
            product = left[-1]
        
        right = list()
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            right = [product * nums[i]] + right
            product = right[0]
        
        left = [1] + left
        right += [1]

        answer = []

        for i in range(len(nums)):
            answer += [left[i] * right[i + 1]]
        


        return answer