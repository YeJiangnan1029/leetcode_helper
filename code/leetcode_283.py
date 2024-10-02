from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        while i<len(nums):
            if nums[i] == 0:  # 找到第一个零元素
                while j < len(nums) and nums[j] == 0: # 找到i之后第一个非零元素
                        j += 1
                if j == len(nums):
                    break
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        return nums



s = Solution()
nums = [4,2,4,0,0,3,0,5,1,0]

print(s.moveZeroes(nums))