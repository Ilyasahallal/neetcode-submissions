import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        frequencys = {}
        for num in nums:
            frequencys[num]= frequencys.get(num,0)+1
        for num,freq in frequencys.items():
            if len(heap) == k :
                if freq > heap[0][0] :
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq,num))
            else :
                heapq.heappush(heap, (freq,num))
        result = []
        for element in heap :
            result.append(element[1])
        return result
        