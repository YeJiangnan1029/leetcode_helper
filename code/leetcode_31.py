from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = -1
        for i in range(len(nums)-1):
            if nums[len(nums)-i-1] > nums[len(nums)-i-2]:
                left = len(nums)-i-2
                break
        if left >=0:
            for i in range(len(nums)-1):
                if nums[len(nums)-i-1] > nums[left]:
                    right = len(nums)-i-1
                    break
            nums[left], nums[right] = nums[right], nums[left]
            i, j = left+1, len(nums)-1
        else:
            i, j = 0, len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1



nums = [1,3,2]
solution = Solution()
print(solution.nextPermutation(nums))