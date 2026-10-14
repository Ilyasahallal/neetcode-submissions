class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        result = 0
        def dfs(r,c):
            nonlocal surface
            if r < 0 or c < 0 or r>n-1 or c>m-1:
                return
            if (r,c) in visited :
                return
            if grid[r][c] == 0 :
                return
            visited.add((r,c))
            surface += 1
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1 and (r,c) not in visited :
                    surface = 0
                    dfs(r,c)
                    result = max(result,surface)
        return result