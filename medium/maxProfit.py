class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0

        n = len(prices)

        hold = [-float('inf')] * n  
        cash = [0] * n  

        hold[0] = -prices[0]  

        for i in range(1, n):
            hold[i] = max(hold[i - 1], cash[i - 1] - prices[i])
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i] - fee) 

        return cash[-1]
