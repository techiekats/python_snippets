#https://leetcode.com/problems/diameter-of-binary-tree/description/
# Definition for a binary tree node.
from typing import Optional
from leetcode_helper_functions import TreeNode, parse_tree

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0  # Global variable for the pattern where we need more that 1 value from recursion level
        def diameter(root: Optional[TreeNode]) -> int:
            nonlocal d
            if root is None:
                return 0
            left_length = diameter(root.left)
            right_length = diameter(root.right)
            root_diameter = left_length + right_length
            if root_diameter > d:
                d = max(d, root_diameter)
            return max(1 + left_length, 1 + right_length)

        diameter(root)
        return d
#test cases
s = Solution()
assert s.diameterOfBinaryTree (parse_tree([1,2,3,4,5])) == 3
assert s.diameterOfBinaryTree(parse_tree([1,2])) == 1