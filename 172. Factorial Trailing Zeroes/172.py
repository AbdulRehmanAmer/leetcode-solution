class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        div = 5
        while n // div:
            res += (n // div)
            div *= 5
        return res
    

#! To Find Number of Trailing 0s
#? x/5 + x/(5^2) + .... + x/(5 ^i)