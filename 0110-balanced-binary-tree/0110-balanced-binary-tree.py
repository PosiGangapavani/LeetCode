# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1
    def height(self,root):
            if root is None:
                return 0
            lhr = self.height(root.left)
            rhr = self.height(root.right)
            if abs(lhr-rhr) > 1:
                return -1
            if lhr == -1:
                return -1
            if rhr == -1:
                return -1
            return max(lhr,rhr)+1
        
            
        