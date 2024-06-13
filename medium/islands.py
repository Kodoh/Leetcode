class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)

        def dfs(i,j):
            if i >= COLS or i < 0 or j >= ROWS or j < 0:
                return False
            elif grid[j][i] == '0' or grid[j][i] == 'v':
                return False
            else:
                grid[j][i] = 'v'
                dfs(i+1,j)
                dfs(i,j+1)
                dfs(i-1,j)
                dfs(i,j-1)


                return True 

        count = 0
        for i in range(COLS):
            for j in range(ROWS):
                if dfs(i,j) == True:
                    count += 1 
        
        return count 