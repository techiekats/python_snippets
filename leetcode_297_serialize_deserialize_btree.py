#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
from leetcode_helper_functions import TreeNode

class Codec:
    ## returns string from tree representation
    def serialize(self, root: TreeNode):
        if not root:
            return ""
        result = ""
        queue = [root]
        nullNode = TreeNode("#")
        while queue:
            x = queue.pop(0)
            result = f"{result},{x.val}"
            if x != nullNode:
                if x.left:
                    queue.append(x.left)
                else:
                    queue.append(nullNode)
                if x.right:
                    queue.append(x.right)
                else:
                    queue.append(nullNode)
        #NOTE: Leaf nodes result in trailing and leading extra characters. Strip them
        return result.rstrip(",#").lstrip(",")

    ## returns tree representation from string
    ##NOTE: to have string data type, use str, not string
    def deserialize(self, data:str):
        if data == "":
            return []
        node_array = data.split(",")
        root = TreeNode(node_array.pop(0))
        queue = [root]

        while queue:
            n = queue.pop(0)
            if any(node_array):
                l = node_array.pop(0)
                if l == "#":
                    n.left = None
                else:
                    n.left = TreeNode(l)
                    queue.append(n.left)
            if any(node_array):
                r = node_array.pop(0)
                if r == "#":
                    n.right = None
                else:
                    n.right = TreeNode(r)
                    queue.append(n.right)
        return root

#test cases
s = Codec()
t1 = s.serialize(None)
assert s.serialize(t1) == ""

node1 = TreeNode(1,TreeNode(2),TreeNode(3))
assert s.serialize(node1) == "1,2,3"
res1 = s.deserialize(s.serialize(node1))
assert res1.val == "1"and res1.left.val == "2" and res1.right.val == "3"

node2 = TreeNode (1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))
assert s.serialize(node2) == "1,2,3,#,#,4,5"
res2 = s.deserialize(s.serialize(node2))
assert res2.val == "1" and res2.left.val == "2" and res2.right.val == "3" and res2.right.left.val == "4" and res2.right.right.val == "5"
assert s.serialize(res2) == "1,2,3,#,#,4,5"

res3 = s.deserialize("1,2")
assert res3.val == "1" and res3.left.val == "2" and res3.right is None

node4 = TreeNode(1, None, TreeNode(2))
assert s.serialize(node4) == "1,#,2"

node5 = TreeNode(1, TreeNode(3,TreeNode(4),TreeNode(5)), TreeNode(2))
assert s.serialize(s.deserialize(s.serialize(node5))) == s.serialize(node5)

node6 = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(5, TreeNode(10), None))
assert s.serialize(s.deserialize(s.serialize(node6))) == s.serialize(node6)
