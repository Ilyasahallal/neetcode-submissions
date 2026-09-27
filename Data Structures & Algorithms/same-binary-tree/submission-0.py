# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1=[p]
        stack2=[q]
        while stack1 or stack2:
            noeud1 = stack1.pop()
            noeud2 = stack2.pop()
            if noeud1 is None and noeud2 is None:
                continue
            if noeud1 is None or noeud2 is None:
                return False
            if noeud1.val != noeud2.val :
                return False
            stack1.append(noeud1.left)
            stack1.append(noeud1.right)
            stack2.append(noeud2.left)
            stack2.append(noeud2.right)
        return True
