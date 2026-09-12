class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l=0
        r=1
        profit=0
        while r<n:
            current_profit = prices[r] - prices[l]
            profit = max(profit,current_profit)
            if prices[r] < prices[l] : 
                l=r
            r=r+1
        return profit 