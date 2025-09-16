# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs (root, target, currentPath):
            if not root:
                return
            currentPath.append(root.val)
            if root.val == target and not root.left and not root.right:
                ans.append(currentPath[:])
                currentPath.pop()
                return
            dfs (root.left, target - root.val,  currentPath)
            dfs (root.right, target - root.val, currentPath)
            node = currentPath.pop()
        dfs (root, targetSum, [])
        return ans

            
            
            