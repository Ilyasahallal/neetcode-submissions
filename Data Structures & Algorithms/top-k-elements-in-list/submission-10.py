class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        frequencys={}
        for i in range(n):
            frequencys[nums[i]]= frequencys.get(nums[i],0)+1
                
        return [key for key, value in sorted(frequencys.items(), key=lambda x: x[1], reverse=True)[:k]]

            

        