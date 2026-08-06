class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        D={}
        for i in range(n):
            difference = target - nums[i]
            D[difference] = i
        for j in range(n):
            if (nums[j] in D ) and (j!=D[nums[j]]) :
                return [j, D[nums[j]]]


        
        

        
        

        
        
   
        
        