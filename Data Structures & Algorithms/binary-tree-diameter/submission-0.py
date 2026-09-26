# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, False )]
        height = {}
        diameter = 0
        if root == None:
            return diameter
        while stack :       
            a = stack.pop()
            noeud = a[0]
            etat = a[1]
            left = noeud.left
            right = noeud.right
            if etat == False :
                stack.append((noeud,True))
                if right :
                    stack.append((right,False))
                if left:
                    stack.append((left,False))
            else :
                if left == None:
                    height[left] = 0
                if right == None :
                    height[right] = 0
                height[noeud] = 1 + max(height[left],height[right])
                diameter = max(diameter , height[left] + height[right])
        return diameter
            
