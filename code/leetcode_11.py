from typing import List


# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_left, max_right = [], []
#         stack_inc_left, stack_inc_right = [], []
#         for i in range(len(height)):
#             h_left = height[i]
#             j = len(height)-i-1
#             h_right = height[j]
#             if not stack_inc_left:
#                 stack_inc_left.append([h_left, i])
#                 stack_inc_right.append([h_right, j])
#                 max_left.append([0, -1])
#                 max_right.append([0, len(height)])
#             else:
#                 if h_left > stack_inc_left[-1][0]:
#                     stack_inc_left.append([h_left, i])
#                     max_left.append([0, -1])
#                 else:
#                     # 二分查找>=h的最小位置
#                     l, r = 0, len(stack_inc_left)-1
#                     while l <= r:
#                         mid = (l+r)//2
#                         if stack_inc_left[mid][0] >= h_left:
#                             r = mid -1
#                         else:
#                             l = mid +1
#                     # l 就是所求的位置
#                     max_left.append(stack_inc_left[l])

#                 if h_right > stack_inc_right[-1][0]:
#                     stack_inc_right.append([h_right, j])
#                     max_right.append([0, len(height)])
#                 else:
#                     # 二分查找>=h的最小位置
#                     l, r = 0, len(stack_inc_right)-1
#                     while l <= r:
#                         mid = (l+r)//2
#                         if stack_inc_right[mid][0] >= h_right:
#                             r = mid -1
#                         else:
#                             l = mid +1
#                     # l 就是所求的位置
#                     max_right.append(stack_inc_right[l])

#         max_area = 0
#         for i in range(len(height)):
#             j = len(height)-i-1
#             area_left = min(height[i], max_left[i][0]) * (i - max_left[i][1])
#             area_right = min(height[i], max_right[j][0]) * (max_right[j][1] - i)
#             area_both = min(max_left[i][0], max_right[j][0]) * (max_right[j][1] - max_left[i][1])
#             max_area = max(max_area, max(area_left, max(area_right, area_both)))
#         return max_area


## 双指针解法
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        while i<j:
            max_area = max(max_area, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i +=1
            else:
                j -=1
        return max_area

s = Solution()
height = [8,20,1,2,3,4,5,6]

print(s.maxArea(height))