from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.tlist = []
        def mid_tra(root):
            if root:
                mid_tra(root.left)
                self.tlist.append(root.val)
                mid_tra(root.right)
        mid_tra(root)
        if len(self.tlist) <= 1:
            return True
        for i in range(len(self.tlist)-1):
            if self.tlist[i] >= self.tlist[i+1]:
                return False
        return True
root = [2,1,3]
solution = Solution()
print(solution.isValidBST(root))