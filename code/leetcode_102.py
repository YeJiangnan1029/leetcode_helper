from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret_list = []
        queue = deque()
        cur_d = 0
        if root:
            queue.append((root, cur_d))
        else:
            return ret_list
        cur_list = []
        while queue:
            node, d = queue.popleft()
            if d == cur_d:
                cur_list.append(node.val)
            else:
                ret_list.append(cur_list)
                cur_d += 1
                cur_list = []
                cur_list.append(node.val)
            if node.left:
                queue.append((node.left, cur_d+1))
            if node.right:
                queue.append((node.right, cur_d+1))
        if cur_list:
            ret_list.append(cur_list)
        return ret_list



root = [3,9,20,null,null,15,7]
solution = Solution()
print(solution.levelOrder(root))