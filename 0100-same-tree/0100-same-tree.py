# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base 1: both are done
        if not p and not q:
            return True
        
        # base 2: only one is done
        if not p or not q:
            return False
        
        # recursive: check roots are equal, recursive on left, recursive on right
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)