from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = -1
        minp = prices[0]
        for p in prices:
            profit = max(profit, p-minp)
            minp = min(minp, p)
        return profit

prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))