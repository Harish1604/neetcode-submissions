import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = set()
        
        heap = [(grid[0][0], 0, 0)]  # (time, r, c)
        visited.add((0, 0))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            time, r, c = heapq.heappop(heap)
            
            if r == n - 1 and c == n - 1:
                return time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # key line
                    heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))