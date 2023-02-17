# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        if root is None:
            return queue
        queue.append(root)
        result = []
        while(queue):
            level = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                
                level.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            result.append(level)
        return result
            