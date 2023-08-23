#  My leetCode Submission: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/solutions/3753770/python-simple-solution-nlgn-solution/
class Solution:
    def minimumSum(self, num: int) -> int:
        num = list(str(num))
        num.sort()
        n1 = num[0] + num[-1]
        n2 = num[1] + num[-2]
        return int(n1) + int(n2)
