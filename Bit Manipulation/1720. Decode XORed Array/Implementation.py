# My LeetCode Submission: https://leetcode.com/problems/decode-xored-array/solutions/3754118/python-built-in-xor-function-concise-solution-efficient-solution/

from operator import xor

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for x in encoded:
            arr.append(xor(arr[-1], x))
        return arr