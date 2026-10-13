class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        perimeter = 0
        def dfs(r,c):
            nonlocal perimeter
            if r < 0 or c < 0 or c > m-1 or r > n-1 :
                perimeter += 1
                return
            if (r,c) in visited :
                return
            if grid[r][c] == 0 :
                perimeter += 1
                return
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            
        for r in range(n):
            for c in range(m):
                if ( grid[r][c] == 1 ):
                    dfs(r,c)
                    return perimeter
                