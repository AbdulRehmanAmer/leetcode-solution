class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = float('-inf')
        temp = prices.pop()
        while prices:
            p = prices.pop()
            ans = max(ans, temp - p)
            temp = max(temp, p)
        return ans if ans > 0 else 0