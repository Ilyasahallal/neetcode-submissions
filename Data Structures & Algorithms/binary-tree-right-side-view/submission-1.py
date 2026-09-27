# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        resultat = []
        if root is None:
            return resultat
        while queue:
            size = len(queue)
            final_node = queue[-1].val
            resultat.append(final_node)
            for i in range(size):
                node = queue.popleft()
                if node.left : 
                    queue.append(node.left)
                if node.right : 
                    queue.append(node.right)
        return resultat



        