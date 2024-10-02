from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ret_list = []
        ret_list.extend(self.inorderTraversal(root.left))
        ret_list.append(root.val)
        ret_list.extend(self.inorderTraversal(root.right))
        return ret_list

root = [1,null,2,3]
solution = Solution()
print(solution.inorderTraversal(root))