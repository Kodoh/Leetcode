class Solution:
    def numTilings(self,N: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (N + 1)
        dp2 = [0] * (N + 1)
        
        dp[0] = 1
        if N >= 1:
            dp[1] = 1
        
        for i in range(2, N + 1):
            dp[i] = (dp[i-1] + dp[i-2] + 2 * dp2[i-1]) % MOD
            dp2[i] = (dp[i-2] + dp2[i-1]) % MOD
        
        return dp[N]

