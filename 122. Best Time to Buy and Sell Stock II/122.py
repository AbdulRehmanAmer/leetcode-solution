class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        temp = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > temp:
                ans += prices[i] - temp

            temp = prices[i]
        return ans
