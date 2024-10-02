from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 维护一个递减的队列
        queue = deque()
        ret = []
        for i in range(len(nums)):
            if i>=k:
                # i = k to nums
                ret.append(queue[0])
                # 出队
                if queue[0] == nums[i-k]:
                    queue.popleft()
            # 入队
            if not queue or nums[i] <= queue[-1]:
                queue.append(nums[i])
            else:
                while queue and queue[-1] < nums[i]:
                    queue.pop()
                queue.append(nums[i])
        ret.append(queue[0])
        return ret

s = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(s.maxSlidingWindow(nums, k))