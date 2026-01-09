# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))
        max_depth = height(root)
        def dfs(root, current_depth):
            if not root:
                return None
            if current_depth == max_depth:
                return root
            left = dfs(root.left, current_depth + 1)
            right = dfs(root.right, current_depth + 1)
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
            return None
        return dfs(root, 1) 

    
