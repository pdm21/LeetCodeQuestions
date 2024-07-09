# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        if not curr or curr == p or curr == q:
            return curr
        
        left = self.lowestCommonAncestor(curr.left, p, q)
        right = self.lowestCommonAncestor(curr.right, p, q)
        
        if left and right:
            return curr
        
        return left or right