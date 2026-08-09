class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hashmap={}
        for i in range(n):
            difference = target - nums[i]
            if difference in hashmap : 
                return [hashmap[difference],i]
            else :
                hashmap[nums[i]] = i