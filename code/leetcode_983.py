from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp[i] 表示满足第i天之前 花费的最小cost
        dp = [0] * 366
        for i in range(len(days)):
            j = i-1
            j1, j7, j30 = 0, 0, 0
            while j>=0:
                if j1 == 0 and days[i]-days[j]>0:
                    j1 = days[j]
                if j7 == 0 and days[i]-days[j]>6:
                    j7 = days[j]
                if j30 == 0 and days[i]-days[j]>29:
                    j30 = days[j]
                    break
                j -= 1

            dp[days[i]] = min(dp[j1]+costs[0], dp[j7]+costs[1], dp[j30]+costs[2])

        # for i in range(1, 366):
        #     if i in days:
        #         i7 = max(i-7, 0)
        #         i30 = max(i-30, 0)
        #         dp[i] = min(dp[i-1]+costs[0], dp[i7]+costs[1], dp[i30]+costs[2])
        #     else:
        #         dp[i] = dp[i-1]
        return dp[days[-1]]


days = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29]
costs = [3,14,50]
solution = Solution()
print(solution.mincostTickets(days, costs))