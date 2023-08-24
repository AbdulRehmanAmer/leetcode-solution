class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Linear Time Solution => O(n)
        track = [-100000]
        length = 0
        for x in nums:
            if track[-1] != x:
                track = [x]
                nums[length] = x
                length += 1
            elif len(track) < 2:
                track += [x]
                nums[length] = x
                length += 1
            
        return length