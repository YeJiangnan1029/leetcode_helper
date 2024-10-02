from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            if cnt == 0:
                x = nums[i]
                cnt = 1
            elif nums[i] == x:
                cnt += 1
            else:
                cnt -= 1
        return x

nums = [3,2,3]
solution = Solution()
print(solution.majorityElement(nums))