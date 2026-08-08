class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        j=0
        while j<n:
            for i in range(j+1,n):
                if (nums[i] + nums[j] == target) :
                    return [j,i]
            j=j+1
            

        
        