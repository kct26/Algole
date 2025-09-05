# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = []
        def dfs (root):
            path.append(str(root.val))
            if not root.left and not root.right:
                ans.append("->".join(path))
            if root.left:
                dfs (root.left)
            if root.right:
                dfs (root.right)
            path.pop()
        dfs (root)
        return ans