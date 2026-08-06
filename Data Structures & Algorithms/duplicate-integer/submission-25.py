class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        D=sorted(nums)
        for i in range(n-1):
            if (D[i] == D[i+1]):
                return True
        return False

            
       
            
        


               
        
        
