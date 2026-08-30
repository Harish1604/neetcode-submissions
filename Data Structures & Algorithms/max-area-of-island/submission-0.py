class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c >= cols or grid[r][c] == 0 or visited[r][c]:
                return 0
            
            visited[r][c] = True

            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    max_area = max(max_area, dfs(r,c))
        return max_area