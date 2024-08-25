class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque() 

        visited = set()

        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
            
        rotted = 0

        while queue:
            i, j, steps = queue.popleft()
            
            if rotted == fresh:
                return steps
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1 and (ni, nj) not in visited:
                    rotted += 1
                    if rotted == fresh:
                        return steps + 1
                    visited.add((ni, nj))
                    queue.append((ni, nj, steps + 1))

        return -1
