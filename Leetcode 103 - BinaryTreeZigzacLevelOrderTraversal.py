# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs approach
        if not root:
            return []
        ans = []
        def bfs (root):
            q = deque([root])
            left_to_right = True
            while q:
                level_size = len(q)
                current = deque()
                for _ in range (level_size):
                    node = q.popleft()
                    if left_to_right:
                        current.append(node.val)
                    else:
                        current.appendleft(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(list(current))
                left_to_right = not left_to_right
        bfs (root)
        return ans