from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        ret_max = 0
        for n in nums:
            l, r = n, n
            if n not in d:
                d[n] = [l, r]
                if n-1 in d:
                    l = d[n-1][0]
                if n+1 in d:
                    r = d[n+1][1]
                d[l] = [l, r]
                d[r] = [l, r]
                ret_max = max(r-l+1, ret_max)
        return ret_max


s = Solution()
nums = [-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]

print(s.longestConsecutive(nums))