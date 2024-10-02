from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l<=r:
            mid = (l+r)//2
            cnt = 0
            for n in nums:
                if n<=mid:
                    cnt += 1
            if cnt <= mid:
                l = mid+1
            else:
                r = mid-1
                ans = mid
        return ans



nums = [1,4,4,3,4,2]
solution = Solution()
print(solution.findDuplicate(nums))