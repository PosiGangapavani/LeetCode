# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.function(root,ans)
        return ans
    def function(self,node,ans):
        if node:
            self.function(node.left,ans)
            ans.append(node.val)
            self.function(node.right,ans)