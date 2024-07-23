class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        start_i = start_j = end_i = end_j = count_zero = 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    end_i = i
                    end_j = j
                elif grid[i][j] == 1:
                    start_i = i
                    start_j = j
                elif grid[i][j] == 0:
                    count_zero += 1

            
        def dfs(i,j,count):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == -1:
                return 0

            if (i,j) == (end_i,end_j):
                return 1 if count == 0 else 0

            grid[i][j] = -1
            total = (dfs(i-1,j,count-1) + dfs(i+1,j,count-1) + dfs(i,j-1,count-1) + dfs(i,j+1,count-1))
            grid[i][j] = 0

            return total

        return dfs(start_i,start_j,count_zero)
