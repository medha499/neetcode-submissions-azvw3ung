class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        new_prices = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                new_prices.append(prices[j] - prices[i])
        if not new_prices:        
            return 0

        return max(0, max(new_prices))

