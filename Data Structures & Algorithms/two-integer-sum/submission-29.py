class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        arr = [(nums[i],i) for i in range(n)]
        arr.sort()
        i=0
        j=n-1
        while i<j :
            if arr[i][0] + arr[j][0] < target :
                i=i+1
            elif arr[i][0] + arr[j][0] > target :
                j=j-1
            else:
                break
        gauche = min(arr[i][1],arr[j][1])
        droit = max(arr[i][1],arr[j][1])
        return [gauche,droit]