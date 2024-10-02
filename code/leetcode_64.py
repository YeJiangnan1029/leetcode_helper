from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        for j in range(n):
            dp[j] = dp[max(j-1, 0)] + grid[0][j]
        for i in range(1, m):
            for j in range(n):
                dp[j] = min(dp[max(j-1, 0)], dp[j]) + grid[i][j]
        return dp[-1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
solution = Solution()
print(solution.minPathSum(grid))