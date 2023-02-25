class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, profit = float("inf"), 0
        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price-minPrice)
        return profit
        