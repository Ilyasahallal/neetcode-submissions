from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited = set()
        result = 0
        queue = deque()
        fresh = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 2 :
                    queue.append((r,c))
                elif grid[r][c] == 1 :
                    fresh +=1
        while queue and fresh > 0:
            size = len(queue)
            for _ in range(size):
                (r,c) = queue.popleft()
                visited.add((r,c))
                if  0<=r+1<n and 0<=c<m  :
                    if grid[r+1][c] == 1 and (r+1,c) not in visited:
                        queue.append((r+1,c))
                        grid[r+1][c] = 2
                        fresh -= 1
                if  0<=r-1<n and 0<=c<m  :
                    if grid[r-1][c] == 1 and (r-1,c) not in visited:
                        queue.append((r-1,c))
                        grid[r-1][c] = 2
                        fresh -= 1
                if  0<=r<n and 0<=c+1<m  :
                    if grid[r][c+1] == 1 and (r,c+1) not in visited:
                        queue.append((r,c+1))
                        grid[r][c+1] = 2
                        fresh -= 1
                if  0<=r<n and 0<=c-1<m  :
                    if grid[r][c-1] == 1 and (r,c-1) not in visited:
                        queue.append((r,c-1))
                        grid[r][c-1] = 2
                        fresh -= 1

            result += 1
        return result if fresh == 0 else -1





