#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    ## returns string from tree representation
    def serialize(self, root: TreeNode):
        if not root:
            return ""
        def inOrderTraverse (node: TreeNode):
            if node is None:
                return "#"
            if not (node.left or node.right):
                return f"{node.val}"
            if not node.right:
                return f"{node.val},{inOrderTraverse(node.left)}"
            return f"{node.val},{inOrderTraverse(node.left)},{inOrderTraverse(node.right)}"
        return inOrderTraverse(root)

    ## returns tree representation from string
    ##NOTE: to have string data type, use str, not string
    def deserialize(self, data:str):
        if data == "":
            return []
        node_array = data.split(",")
        queue = []
        x= node_array.pop(0)
        queue.append (x)
        root = None
        while queue:
            x = queue.pop(0)
            n = TreeNode(x)
            if root is None:
                root = n
            if any(node_array):
                l = node_array.pop(0)
                if l == "":
                    n.left = None
                else:
                    n.left = TreeNode(l)
                queue.append(l)
            if any(node_array):
                r = node_array.pop(0)
                if r == "":
                    n.right = None
                else:
                    n.right = TreeNode(r)
                queue.append(r)
        return root

#test cases
s = Codec()
t1 = s.serialize(None)
print (t1)
assert s.serialize(t1) == ""

node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)
print (s.serialize(node1))
assert s.serialize(node1) == "1,2,3"
res1 = s.deserialize(s.serialize(node1))
assert res1.val == "1"
assert res1.left.val == "2"
assert res1.right.val == "3"

node2 = TreeNode (1)
node2.left = TreeNode(2)
node2.right = TreeNode(3)
node2.right.left = TreeNode(4)
node2.right.right = TreeNode(5)
print (s.serialize(node2))
assert s.serialize(node2) == "1,2,3,#,#,4,5"
res2 = s.deserialize(s.serialize(node2))
assert res2.val == 1
##TODO: remaining

