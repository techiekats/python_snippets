#https://leetcode.com/problems/binary-tree-tilt/description/
from typing import Optional
from leetcode_helper_functions import TreeNode, parse_tree

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # CHALLENGE was how to pass both sum and tilt upward. Introduce a global variable for such patterns
        tilt = 0
        def findSum(node: Optional[TreeNode]) -> int:
            nonlocal tilt
            if node is None:
                return 0
            left_sum = 0
            right_sum = 0
            if node.left is not None:
                left_sum = findSum(node.left)
            if node.right is not None:
                right_sum = findSum(node.right)
            # Declares intent to modify the parent variable
            tilt += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum
        findSum(root)
        return tilt
#test cases
s = Solution()
##TODO: create TreeNode from array
t1 = parse_tree([1,2,3])
t2 = parse_tree([4,2,9,3,5,None,7])
t3 = parse_tree([21,7,14,1,1,2,2,3,3])

assert s.findTilt(t2) == 15
assert s.findTilt(t1) == 1
assert s.findTilt(t3) == 9