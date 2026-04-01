#https://leetcode.com/problems/binary-tree-tilt/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # CHALLENGE was how to pass both sum and tilt upward. Introduce a global variable for such patterns
    tilt = 0

    def findSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_sum = 0
        right_sum = 0
        if root.left is not None:
            left_sum = self.findSum(root.left)
        if root.right is not None:
            right_sum = self.findSum(root.right)
        self.tilt += abs(left_sum - right_sum)
        return root.val + left_sum + right_sum

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.findSum(root)
        return self.tilt
#test cases
s = Solution()
##TODO: create TreeNode from array
#assert s.findSum([1,2,3]) == 1