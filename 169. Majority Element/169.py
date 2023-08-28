from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Through HASHING
        # Since we have no problem for hashing collision, we can maintain our hashtable simply.
        counts = Counter(nums)

        for i in counts:
            if counts[i] > len(nums) // 2: return i