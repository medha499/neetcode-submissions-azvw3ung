class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## when Im at 10 - check any #s after that are greater? If not, 
        ## move to # number 

        min_price = float('inf')
        max_profit = 0
        for price in prices:
        # best buy so far
            min_price = min(min_price, price)

        # profit if we sold today
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit

            
        
          