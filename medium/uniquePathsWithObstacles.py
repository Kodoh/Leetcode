def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0
    
    COLS = len(obstacleGrid[0])
    ROWS = len(obstacleGrid)
    
    dp = [[-1] * COLS for _ in range(ROWS)]
    
    def dfs(i, j):
        if i < 0 or j < 0 or i >= ROWS or j >= COLS or obstacleGrid[i][j] == 1:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        if i == ROWS - 1 and j == COLS - 1:
            return 1
        
        right_paths = dfs(i, j + 1)
        down_paths = dfs(i + 1, j)
        
        dp[i][j] = right_paths + down_paths
        
        return dp[i][j]
    
    return dfs(0, 0)


print(uniquePathsWithObstacles([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))
