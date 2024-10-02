from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def getBST(nums, l, r):
            if l>r:
                return None
            if l==r:
                return TreeNode(nums[l])
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = getBST(nums, l, mid-1)
            root.right = getBST(nums, mid+1, r)
            return root
        return getBST(nums, 0, len(nums)-1)


nums = [-10,-3,0,5,9]
solution = Solution()
print(solution.sortedArrayToBST(nums))