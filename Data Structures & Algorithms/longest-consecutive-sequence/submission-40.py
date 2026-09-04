class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        s=set(nums)
        l=0
        result=l
        for i in range(n):
            l=0
            num=nums[i]
            if nums[i]-1 in s:
                pass
            else :
                while num in s:
                    l=l+1
                    num=num+1
            if l>result:
                result=l
        return result
                
        