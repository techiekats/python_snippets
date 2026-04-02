#https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional
from leetcode_helper_functions import TreeNode, parse_tree
import sys

class Solution:
    def isValidBST(self, root: Optional[TreeNode], min=-sys.maxsize - 1, max=sys.maxsize) -> bool:
        if root is None:
            return True
        if root.val <= min or root.val >= max:
            return False
        ## NOTE: the min is always unbounded for the left tree and max is unbounded for the right tree
        return self.isValidBST(root.left, min, root.val) and self.isValidBST(root.right, root.val, max)

#test cases
s = Solution()
assert s.isValidBST(parse_tree([2,1,3]))
assert s.isValidBST(parse_tree([5,1,4,None,None,3,6])) == False
