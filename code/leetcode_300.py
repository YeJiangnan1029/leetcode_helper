import heapq
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示长度为i的最长递增子序列的最小末尾元素
        dp = []
        for i in range(len(nums)):
            l, r = 0, len(dp)-1
            while l<=r:
                mid=(l+r)//2
                if nums[i] > dp[mid]:
                    l = mid+1
                else:
                    r = mid-1
            if l >= len(dp):
                dp.append(nums[i])
            else:
                dp[l] = min(dp[l], nums[i])
        return len(dp)


nums = [10,9,2,5,3,7,101,18]
solution = Solution()
print(solution.lengthOfLIS(nums))