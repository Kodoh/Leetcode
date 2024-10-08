class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        dp.extend([amount+1]*amount)
        
        for coin in coins:
            for i in range(coin,amount+1):
                dp[i] = min(dp[i],dp[i-coin]+1)

        if dp[-1] == amount + 1:
            return -1

        return dp[-1]
