class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = -1
        maxProfit = 0
        for i,price in enumerate(prices):
            if minVal == -1:
                minVal = price
            else:
                minVal = min(minVal, price)  
            maxProfit = max(price-minVal, maxProfit)
        return maxProfit