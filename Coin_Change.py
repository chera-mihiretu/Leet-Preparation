from typing import *
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        last_index = amount + 1
        dp = [float('inf') for _ in range(last_index)]
        dp[0] = 0
        for i in range(last_index):
            if dp[i] != float('inf'):
                for coin in coins:
                    if i + coin < last_index:
                        dp[i+coin] = min(dp[i] + 1, dp[i + coin])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount] 