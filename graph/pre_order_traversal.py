# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        result = []
        if root == None:
            return []
        while stack:
            root = stack.pop()
            if root.val is not None:
                result.append(root.val)
            if root.right != None:
                stack.append(root.right)
            if root.left != None:
                stack.append(root.left)
        return result
#     Using Morris Algorithm for Pre-Order Traversal'

        result = []
        while root:
            if root.left == None:
                result.append(root.val)
                root = root.right
            else:
                current = root.left
                while current.right != None and current.right != root:
                    current = current.right

                if current.right is root:
                    current.right = None
                    root = root.right
                else:
                    result.append(root.val)
                    current.right = root
                    root = root.left
        return result
