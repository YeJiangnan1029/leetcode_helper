from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # max_ret = nums[0]
        # _sum = 0
        # for n in nums:
        #     _sum += n
        #     if _sum <0:
        #         _sum = 0
        #         max_ret = max(max_ret, n)
        #         continue
        #     else:
        #         max_ret = max(max_ret, _sum)
        # return max_ret
    
    # 分治法
        return self.my_maxSubArray(nums, 0, len(nums)-1)[0]

    def my_maxSubArray(self, nums: List[int], l, r) -> tuple[int, int, int, int]:
        if l == r:
            return nums[l], nums[l], nums[l], nums[l]
        
        # l < r
        mid = (l+r)//2
        msum_1, lsum_1, rsum_1, isum_1 = self.my_maxSubArray(nums, l, mid)
        msum_2, lsum_2, rsum_2, isum_2 = self.my_maxSubArray(nums, mid+1, r)
        isum = isum_1 + isum_2
        lsum = max(lsum_1, isum_1+lsum_2)
        rsum = max(rsum_2, isum_2+rsum_1)
        msum = max(rsum_1+lsum_2, max(msum_1, msum_2))
        return msum, lsum, rsum, isum


s = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))