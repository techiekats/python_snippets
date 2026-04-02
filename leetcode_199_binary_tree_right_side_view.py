#https://leetcode.com/problems/binary-tree-right-side-view/description/

from typing import List, Optional
from collections import deque
from leetcode_helper_functions import TreeNode, parse_tree

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        queue = deque([(root, 0)])
        while queue:
            (node, level) = queue.popleft()
            if level == len(result):
                result.append(node.val)
            else:
                result[level] = node.val

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return result
#test cases
s = Solution()
assert s.rightSideView(parse_tree([1,2,3,None,5,None,4])) == [1,3,4]
assert s.rightSideView(parse_tree([1,2,3,4,None, None, None,5])) == [1,3,4,5]
assert s.rightSideView(parse_tree([1,None,3])) == [1,3]
