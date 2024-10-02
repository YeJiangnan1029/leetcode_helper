from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = defaultdict(int)
        for n in nums:
            fre[n] += 1
        l = [it for it in fre.items()]
        l = sorted(l, key=lambda x: x[1], reverse=True)
        return [x[0] for x in l[:k]]
        

nums = [1,1,1,2,2,3]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))