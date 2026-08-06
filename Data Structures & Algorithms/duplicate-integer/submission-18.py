class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        D=set()
        for i in range(n):
            D.add(nums[i])
        if (len(D) < n) :
            return True
        return False

            
       
            
        


               
        
        
