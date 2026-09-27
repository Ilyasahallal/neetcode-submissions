# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = [(root , False)]
        height = {}
        if root == None:
            return True
        while stack :
            a= stack.pop()
            noeud = a[0]
            etat = a[1]
            left = noeud.left
            right = noeud.right
            if etat == False:
                stack.append((noeud,True))
                if left :
                    stack.append((left, False))
                if right:
                    stack.append((right,False))
            else:
                height_left = height[left] if left else 0
                height_right = height[right] if right else 0
                height[noeud] = 1 + max(height_left,height_right)
                difference = abs (height_left - height_right)
                if difference > 1 :
                    return False
        return True

        