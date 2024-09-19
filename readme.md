## 用法
这个工具用于在leetcode刷题时根据查询到的题目信息自动生成python代码的模板，避免本地编写/调试时重复的复制粘贴劳动


主函数在 `gen_code_template.py`

配置第6~7行 `problem_id={题号}, output_folder={输出代码的文件夹}`

运行"
```
python gen_code_template.py
```

## Samples
题号为`2`时，输出模板文件为 `leetcode_2.py`
```
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass

l1 = [2,4,3]
l2 = [5,6,4]
solution = Solution()
print(solution.addTwoNumbers(l1, l2))
```

题号为`15`时，输出模板文件为 `leetcode_15.py`
```
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))
```