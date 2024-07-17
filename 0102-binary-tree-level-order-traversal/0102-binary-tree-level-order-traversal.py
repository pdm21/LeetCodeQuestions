# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # create result array, initialize a queue
        res = []
        q = collections.deque()
        q.append(root)
        # while the q is nonempty
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                # if node is not null
                if node:
                    level.append(node.val)
                    q.append(node.left) # if null, checked in if statement next loop
                    q.append(node.right) # if null, checked in if statement next loop
            # if level is nonempty, do not want to add blank array
            if level:
                res.append(level)
        return res