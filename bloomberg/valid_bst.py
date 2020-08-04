# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.bstWithMinMax(root, float('-inf'), float('inf'))
        
    def bstWithMinMax(self, node, minimum, maximum):
        if not node:
            return True
        if node.val <= minimum or node.val >= maximum:
            return False
        return self.bstWithMinMax(node.left, minimum, node.val) and self.bstWithMinMax(node.right, node.val, maximum)