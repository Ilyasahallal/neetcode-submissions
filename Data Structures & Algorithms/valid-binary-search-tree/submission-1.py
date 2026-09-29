# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        moins_infini = float('-inf')
        plus_infini = float('+inf')
        stack = [(root , moins_infini , plus_infini)]
        while stack :
            a = stack.pop()
            node = a[0]
            min = a[1]
            max = a[2]
            if node.val <= min :
                return False
            if node.val >= max :
                return False
            if node.left :
                stack.append((node.left,min,node.val))
            if node.right :
                stack.append((node.right,node.val,max))
        return True
