class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minPrice = prices[0]
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                profit = max(profit, price - minPrice) 
        return profit          

        