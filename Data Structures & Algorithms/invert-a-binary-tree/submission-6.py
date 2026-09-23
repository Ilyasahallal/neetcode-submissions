# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        stack = [root]

        if root is None:
            return root

        while stack :
            a=stack.pop()
            if a.left :
                stack.append(a.left)
            if a.right :
                stack.append(a.right)

            a.right,a.left=a.left,a.right

        return root
        