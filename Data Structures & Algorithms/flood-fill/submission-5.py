class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        visited = set()
        reference = image[sr][sc]
        def dfs(r,c):
            if r < 0 or c < 0 or r > n-1 or c > m-1:
                return
            if (r,c) in visited:
                return
            if image[r][c] != reference :
                return
            image[r][c] = color
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        dfs(sr,sc)
        return image
        