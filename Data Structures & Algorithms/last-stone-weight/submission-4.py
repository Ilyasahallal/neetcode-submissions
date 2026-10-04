import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones : 
            heapq.heappush(heap,-stone)
        
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            difference = first - second
            if difference != 0:
                heapq.heappush(heap,difference)
        return -heap[0] if heap else 0   
        