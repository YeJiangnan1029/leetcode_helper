from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        reach = nums[0]
        max_range = reach
        if max_range >= len(nums)-1:
            return 1
        jc = 1
        i = 1
        while i < len(nums):
            if i + nums[i] > max_range:
                max_range = i + nums[i]
                if max_range >= len(nums)-1:
                    return jc+1
            if i == reach:
                jc += 1
                reach = max_range
            i+=1

        

nums = [1,1,1,1,1,1,1]
solution = Solution()
print(solution.jump(nums))