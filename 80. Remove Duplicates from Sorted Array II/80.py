class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        track = dict()
        for x in nums:# => O(n)
            track[x] = 0
        
        for x in nums:# => O(n)
            track[x] += 1
        
        
        length = 0
        for x in track.keys():# => O(n)
            if track[x] == 1:
                nums[length] = x

            elif track[x] >= 2:
                nums[length] = x
                length += 1
                nums[length] = x

            track[x] = 0
            length += 1

        return length
                