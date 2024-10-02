from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # nlogn
        ret_list = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                c = -nums[i]-nums[j]
                while k>j and nums[k] > c:
                    k -= 1
                # nums[k] <= c
                if j >= k:
                    break
                if nums[k] == c:
                    ret_list.append([nums[i], nums[j], nums[k]])
                j+=1
                while j < len(nums) and nums[j] == nums[j-1]:
                    j += 1
        return ret_list

nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))