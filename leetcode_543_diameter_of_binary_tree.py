#https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    d = 0  # Global variable for the pattern where we need more that 1 value from recursion level

    def diameter(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_length = self.diameter(root.left)
        right_length = self.diameter(root.right)
        root_diameter = left_length + right_length
        if root_diameter > self.d:
            self.d = max(self.d, root_diameter)
        return max(1 + left_length, 1 + right_length)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        self.diameter(root)
        return self.d
#test cases
s = Solution()
#TODO: parse these arrays into TreeNodes
# assert s.diameter ([1,2,3,4,5]) == 3
# assert s.diameter([1,2]) == 3