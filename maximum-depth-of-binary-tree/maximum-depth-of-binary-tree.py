# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        leftans = 0
        rightans = 0
        if root is None:
            return 0 
        leftans = max(leftans,self.maxDepth(root.left))
        rightans = max(rightans,self.maxDepth(root.right))
        return max(leftans,rightans) + 1
        
        