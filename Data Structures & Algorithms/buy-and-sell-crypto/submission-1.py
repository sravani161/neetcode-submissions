class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = float("-inf")
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit,price-min_price)
        return max_profit