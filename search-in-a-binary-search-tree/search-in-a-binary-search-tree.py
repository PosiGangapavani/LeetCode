
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def search(self,root,val):
        if root == None:
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left,val)
            

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(root,val)
        
        