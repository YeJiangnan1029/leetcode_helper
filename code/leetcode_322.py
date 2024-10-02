from functools import cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 100000
        dp = [MAX] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return dp[amount] if dp[amount] != MAX else -1

coins = [2]
amount = 3
solution = Solution()
print(solution.coinChange(coins, amount))