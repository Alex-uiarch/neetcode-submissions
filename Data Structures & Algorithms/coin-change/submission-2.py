class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            uns = []

            for coin in coins:
                if coin <= i:
                    uns.append(1 + dp[i - coin])
                elif coin > i:
                    uns.append(dp[i])

                dp[i]= min(uns)


        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
                
