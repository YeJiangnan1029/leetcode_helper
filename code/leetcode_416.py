from functools import cache
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target = target >> 1
        @cache
        def dp(i, t):
            if i>len(nums)-1 or t < 0:
                return False
            if t == 0:
                return True
            return dp(i+1, t-nums[i]) or dp(i+1, t)
        return dp(0, target)
            


nums = [1,5,11,5]
solution = Solution()
print(solution.canPartition(nums))