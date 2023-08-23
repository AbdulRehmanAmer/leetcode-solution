# My LeetCode Submission: https://leetcode.com/problems/split-a-string-in-balanced-strings/solutions/3753931/python-easiest-efficient-solution-containers-linear-time-solution/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_container, r_container = 0, 0
        balanced_substrings = 0
        for x in s:
            if x == 'L':
                l_container += 1
            else:
                r_container += 1
            if l_container == r_container:
                balanced_substrings += 1
                l_container, r_container = 0, 0

        return balanced_substrings