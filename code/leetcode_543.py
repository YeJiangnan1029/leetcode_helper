from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def getd(root):
            if root is not None:
                sl, dl, sr, dr = 0,0,0,0
                if root.left:
                    sl, dl = getd(root.left)
                    sl += 1
                if root.right:
                    sr, dr = getd(root.right)
                    sr += 1
                ms = max(sl, sr)
                md = max(sl + sr, max(dl, dr))
                return ms, md
            else:
                return 0, 0  # 单边最长距离， 双边最长距离
        ms, md = getd(root)
        return max(ms, md)

root = [1,2,3,4,5]
solution = Solution()
print(solution.diameterOfBinaryTree(root))