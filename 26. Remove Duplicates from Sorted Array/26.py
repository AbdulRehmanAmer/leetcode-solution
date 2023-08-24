from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        length = 0
        for x in counts.keys():
            nums[length] = x
            length += 1
        return length
        




