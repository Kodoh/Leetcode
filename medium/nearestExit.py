class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque([(entrance[0], entrance[1], 0)]) 
        visited = set((entrance[0], entrance[1]))
        
        while queue:
            i, j, steps = queue.popleft()
            
            if ([i, j] != entrance) and (i == 0 or j == 0 or i == rows - 1 or j == cols - 1):
                return steps
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] == '.' and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    queue.append((ni, nj, steps + 1))
        
        return -1  
