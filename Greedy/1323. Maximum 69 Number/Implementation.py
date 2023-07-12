#  My LeetCode Submission: https://leetcode.com/problems/maximum-69-number/solutions/3754026/python-concise-solution/
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        for i in range(len(num)):
            if num[i] == "6":
                num = num[ : i] + "9" + num[i + 1 : ]
                
                break

        return int(num)
