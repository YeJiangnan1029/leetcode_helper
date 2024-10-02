from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, n in enumerate(nums):
            if target - n not in d:
                d[n] = i
            else:
                return [i, d[target - n]]
        

s = Solution()
nums = [2,7,11,15]
target = 9

print(s.twoSum(nums, target))