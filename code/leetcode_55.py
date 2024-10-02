from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_range = 0
        i = 0
        while i <= max_range:
            if i == len(nums)-1:
                return True
            max_range = max(max_range, i+nums[i])
            i += 1
        return False


nums = [3,2,1,0,4]
solution = Solution()
print(solution.canJump(nums))