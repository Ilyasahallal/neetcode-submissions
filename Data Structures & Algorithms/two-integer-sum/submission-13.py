class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        L=[]
        hashmap={}
        for i in range(n):
            hashmap[nums[i]]=i
        for i in range(n):
            difference=target-nums[i]
            if (difference in hashmap) and (i!=hashmap[difference]) : 

                L.append(min(i,hashmap[difference]))
                L.append(max(i,hashmap[difference]))
                return L


        
        

        
        
   
        
        