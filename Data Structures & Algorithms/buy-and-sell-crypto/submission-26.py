class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_price=prices[0]
        profit=0
        for i in range(1,n):
            current_profit = prices[i] - min_price
            if (current_profit) > profit :
                profit = current_profit
            if prices[i] < min_price:
                min_price = prices[i]
        return profit 

