class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        ROWS, COLS = len(board), len(board[0])
        
        # Use a new board to keep track of visited cells
        new = [[True for _ in range(COLS)] for _ in range(ROWS)]
        seen = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i, j) in seen or board[i][j] == 'X':
                return
            seen.add((i, j))
            if board[i][j] == 'O':
                new[i][j] = False
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        # Start DFS from 'O's on the borders
        for i in range(ROWS):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][COLS - 1] == 'O':
                dfs(i, COLS - 1)
        
        for j in range(COLS):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[ROWS - 1][j] == 'O':
                dfs(ROWS - 1, j)
        
        # Flip unmarked 'O' to 'X'
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and new[i][j]:
                    board[i][j] = 'X'