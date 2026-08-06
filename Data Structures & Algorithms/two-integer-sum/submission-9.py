class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        L=[]
        for i in range(n):
            for j in range(i+1,n):
                if (nums[i] + nums[j] == target ) and (i!=j) :
                    L.append(min(i,j))
                    L.append(max(i,j))
                    return L 
   
        
        