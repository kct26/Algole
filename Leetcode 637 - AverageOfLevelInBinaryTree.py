from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q:
            size_level = len(q)
            total_level = 0
            for i in range (size_level):
                node = q.popleft()
                total_level += node.val
                if i == size_level - 1:
                    ans.append(total_level/size_level)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans 