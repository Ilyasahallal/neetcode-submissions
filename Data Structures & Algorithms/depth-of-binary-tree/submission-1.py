# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None : 
            return 0
        stack = [(root,1)]
        depth = 1
        while stack :
            a = stack.pop()
            depth = max(depth , a[1])
            if a[0].left :
                stack.append((a[0].left , a[1] + 1))
            if a[0].right:
                stack.append((a[0].right, a[1] + 1))

        return depth
        