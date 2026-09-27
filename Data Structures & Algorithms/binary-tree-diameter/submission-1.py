# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root,False)]
        diameter = 0
        height={}
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
                if left:
                    stack.append((left,False))
                if right:
                    stack.append((right,False))
            elif etat == True :
                left_height = height[left] if left else 0
                right_height = height[right] if right else 0
                height[noeud] = 1 + max(left_height , right_height)
                diameter = max ( diameter , right_height + left_height)
            
        return diameter    
                