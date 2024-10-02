from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = [], []
        for i in range(len(height)):
            if i == 0:
                max_left.append(0)
                max_right.append(0)
            else:
                h_l = height[i-1]
                h_r = height[len(height)-i]
                max_left.append(max(max_left[-1], h_l))
                max_right.append(max(max_right[-1], h_r))
        sum_trap = 0
        for i in range(len(height)):
            sum_trap += max(min(max_left[i], max_right[len(height)-i-1]) - height[i], 0)
        return sum_trap                            

height = [4,2,3]
s = Solution()
print(s.trap(height))