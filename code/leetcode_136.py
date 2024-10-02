from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for num in nums:
            r ^= num
        return r

nums = [2,2,1]
solution = Solution()
print(solution.singleNumber(nums))