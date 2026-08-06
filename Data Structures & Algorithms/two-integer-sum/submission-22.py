class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        zabba=None
        D={}
        for i in range(n):
            if ( nums[i] in D ) and (i != D[nums[i]] ) :
                return [D[nums[i]],i]
            D[target - nums[i]] = i
            
        return zabba

            


        
        

        
        

        
        
   
        
        