# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maximum = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.maximum
    def height(self,root):
        
        if root is None:
            return 0
        lhr = self.height(root.left)
        rhr = self.height(root.right)
        if lhr+rhr > self.maximum:
            self.maximum = lhr + rhr 
        if lhr > rhr:
            return lhr + 1
        return rhr + 1