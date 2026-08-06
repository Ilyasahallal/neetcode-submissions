class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        l,r=0,1
        profit=0
        max_profit=0
        while r<n:
            if (prices[l]-prices[r])<0 :
                profit=prices[r]-prices[l]
                max_profit=max(profit,max_profit)
            else:
                l=r
            r+=1
        return max_profit

            
