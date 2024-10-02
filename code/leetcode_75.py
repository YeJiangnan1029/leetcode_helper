from collections import defaultdict
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fre = defaultdict(int)
        for n in nums:
            fre[n] += 1
        for i in range(1, 3):
            fre[i] += fre[i-1]
        for i in range(len(nums)):
            if i < fre[0]:
                nums[i] = 0
            elif i < fre[1]:
                nums[i] = 1
            else:
                nums[i] = 2

nums = [2,0,2,1,1,0]
solution = Solution()
print(solution.sortColors(nums))