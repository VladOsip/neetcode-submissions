class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        day = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < day:
                day = prices[i]
            profit = max(profit, prices[i]-day)
        
        return profit