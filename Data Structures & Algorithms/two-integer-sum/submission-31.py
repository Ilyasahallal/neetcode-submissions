class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        arr = [(nums[i],i) for i in range(n)]
        arr.sort()
        i=0
        j=n-1
        while i<j :
            total = arr[i][0] + arr[j][0]
            if total < target :
                i=i+1
            elif total > target :
                j=j-1
            else:
                return sorted([arr[i][1],arr[j][1]])
  