class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        a=0
        b=n
        while a<b:
            m=(a+b)//2
            if target < nums[m] :
                b=m
            elif target > nums[m] :
                a=m+1
            else :
                return m
        return -1

