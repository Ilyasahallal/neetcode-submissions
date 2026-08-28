class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        frequencys={}
        for i in range(n):
            frequencys[nums[i]]= frequencys.get(nums[i],0)+1
        buckets=[[] for i in range(n+1)]
        result = []
        for num,freq in frequencys.items():
            buckets[freq].append(num)
        for i in range(n,-1,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k :
                    return result
            


