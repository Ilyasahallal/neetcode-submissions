class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=0
        max_rights={}
        max_right=0
        for i in range(n-1,0,-1):
            if height[i] > max_right : 
                max_right = height[i]
            max_rights[i]=max_right
        result=0
        for i in range(1,n-1):
            if height[i-1] > max_left :
                max_left = height[i-1]
            water= min (max_left,max_rights[i]) - height[i]
            if water>0:
                result = result + water
        return result


