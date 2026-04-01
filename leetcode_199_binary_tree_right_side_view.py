#https://leetcode.com/problems/binary-tree-right-side-view/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
from collections import deque
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
##TODO: contruct tree from array
# assert s.rightSideView([1,2,3,null,5,null,4]) == [1,3,4]
# assert s.rightSideView([1,2,3,4,null,null,null,5]) == [1,3,4,5]
# assert s.rightSideView([1,null,3]) == [1,3]
