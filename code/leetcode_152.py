from math import inf
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] 表示以nums[i]结尾的最大乘积子数组的乘积
        MAX = nums[0]
        max_dp = nums[0]
        min_dp = nums[0]
        for i in range(1, len(nums)):
            max_dp, min_dp = max(max_dp*nums[i], min_dp*nums[i], nums[i]), min(max_dp*nums[i], min_dp*nums[i], nums[i])
            MAX = max(MAX, max_dp)
        return MAX

nums = [-4,-3,-2]
solution = Solution()
print(solution.maxProduct(nums))