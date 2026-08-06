class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums_s= sorted(nums)
        L=[]
        for i in range(n):
            target = -nums_s[i]
            if i>0 and nums_s[i]==nums_s[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                s=nums_s[l]+nums_s[r]
                if (s== target ) and (i!=l and i!=r) :
                    L.append([nums_s[l],nums_s[r],nums_s[i]])
                    l+=1
                    r-=1
                    while l < r and nums_s[l] == nums_s[l - 1]:
                        l += 1
                    while l < r and nums_s[r] == nums_s[r + 1]:
                        r -= 1

                
                elif s>target :
                    r=r-1
                else:
                    l=l+1
        return L

        