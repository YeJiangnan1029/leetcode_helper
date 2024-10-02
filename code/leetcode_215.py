import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k+1):
            t = heapq.heappop(nums)
        return t

nums = [3,2,1,5,6,4]
k = 2
solution = Solution()
print(solution.findKthLargest(nums, k))