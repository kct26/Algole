"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:            
            level_size = len(q)
            current = []
            for i in range (level_size):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
                current.append(node.val)
            ans.append(current)
        return ans