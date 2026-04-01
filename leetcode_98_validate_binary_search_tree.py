#https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min=-sys.maxsize - 1, max=sys.maxsize) -> bool:
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        ## NOTE: the min is always unbounded for the left tree and max is unbounded for the right tree
        return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)
