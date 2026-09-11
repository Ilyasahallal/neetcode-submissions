class Solution:
    def trap(self, height: List[int]) -> int:
        #TwoPointers
        n=len(height)
        left=0
        right=n-1
        max_left=left
        max_right=right
        result=0
        while left<right:
            if height[max_left]<height[max_right]:
                water = height[max_left] - height[left]
                if water > 0 : 
                    result = result + water
                left=left+1
                if height[left] > height[max_left] : 
                    max_left = left
            elif height[max_right]<=height[max_left]:
                water = height[max_right] - height[right]
                if water > 0:
                    result = result + water
                right=right-1
                if height[right] > height[max_right] :
                    max_right = right
        return result


            
        