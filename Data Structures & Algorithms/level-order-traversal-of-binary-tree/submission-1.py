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
            size=len(queue)
            L=[]
            for i in range(size):
                node = queue.popleft()
                L.append(node.val)
                if node.left:  
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            resultat.append(L)
        return resultat



        