from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+1)
        for i in range(len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-2]

nums = [2,7,9,3,1]
solution = Solution()
print(solution.rob(nums))