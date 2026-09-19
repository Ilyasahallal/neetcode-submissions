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
        if target > nums[m] :
            return m+1
        elif m==0 :
            return 0
        return m
        