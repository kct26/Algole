# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        res = None
        count = 0
        def dfs (root):
            nonlocal res, count
            if not root or res is not None:
                return 
            dfs (root.left)
            count += 1
            if count == k:
                res = root.val
                return
            dfs (root.right)
        dfs(root)
        return res
                
            
        