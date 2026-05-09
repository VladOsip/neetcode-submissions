class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        left = right = 0
        max_return = 0
        while right < len(prices):
            if prices[left] <= prices[right]:
                temp = prices[right] - prices[left]
                max_return = max(max_return,temp)
            else:
                left = right
            right+=1
        return max_return



