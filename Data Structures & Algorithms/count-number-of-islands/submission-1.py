class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        result = 0
        visited = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r > n-1 or c > m-1:
                return
            if (r,c) in visited:
                return
            if grid[r][c] == "0":
                return
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(n):
            for c in range(m):
                if (grid[r][c] == "1") and ((r,c) not in visited):
                    dfs(r,c)
                    result += 1
        return result

        