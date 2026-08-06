class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            L=[]
            for j in range(n):
                if nums[j] == nums[i] : 
                    L.append(j);
            if len(L)> 1 :
                return True
        return False


               
        
        
