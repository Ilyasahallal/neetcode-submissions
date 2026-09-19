class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        a=0
        b=n-1
        while a<=b:
            m=(a+b)//2
            if target < nums[m] :
                b=m-1
            elif target > nums[m] :
                a=m+1
            else :
                return m
        return a
        