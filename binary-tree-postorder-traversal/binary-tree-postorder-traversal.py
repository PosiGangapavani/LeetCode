# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,ans):
        if root:
            if root.left:
                self.check(root.left,ans)
            if root.right:
                self.check(root.right,ans)
            ans.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.check(root,ans)
        return ans
        