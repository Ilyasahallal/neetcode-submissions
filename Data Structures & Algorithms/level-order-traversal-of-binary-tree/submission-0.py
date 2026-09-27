# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        resultat = []
        queue = deque([root])
        if root is None:
            return []
        while queue :
            level = []
            L=[]
            while queue:
                node = queue.popleft()
                level.append(node)
                L.append(node.val)
            resultat.append(L)
            for node in level:
                if node.left:  
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return resultat



        