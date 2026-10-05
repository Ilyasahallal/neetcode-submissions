import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(heap,(-distance,[x,y]))
            if len(heap) > k :
                heapq.heappop(heap)
        return [element[1] for element in heap]
        