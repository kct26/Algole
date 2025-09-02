class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0]
        profit = 0
        for price in prices:
            if price < current:
                current = price
            profit = max (profit, price - current)
        return profit