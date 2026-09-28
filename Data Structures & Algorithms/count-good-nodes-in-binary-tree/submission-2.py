# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root , root.val)]
        resultat = 0
        if root is None :
            return 0
        while stack :
            a = stack.pop()
            node = a[0]
            maximum = a[1]
            if node.val >= maximum :
                resultat = resultat + 1
                maximum = node.val
            if node.left : 
                stack.append((node.left,maximum))
            if node.right :
                stack.append((node.right,maximum))
        return resultat
        