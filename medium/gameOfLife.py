class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Modify the board in-place according to the rules of the Game of Life.
        """
        def inbounds(i, j, m, n):
            return 0 <= i < m and 0 <= j < n

        directions = [
            (-1, -1),  # Top-left
            (-1, 0),   # Top
            (-1, 1),   # Top-right
            (0, -1),   # Left
            (0, 1),    # Right
            (1, -1),   # Bottom-left
            (1, 0),    # Bottom
            (1, 1)     # Bottom-right
        ]

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                one_count = 0
                for direction in directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    if inbounds(new_i, new_j, m, n):
                        if board[new_i][new_j] == 1 or board[new_i][new_j] == -1:
                            one_count += 1


                if board[i][j] == 1 and (one_count < 2 or one_count > 3):
                    board[i][j] = -1  

                if board[i][j] == 0 and one_count == 3:
                    board[i][j] = 2  

        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0  
                elif board[i][j] == 2:
                    board[i][j] = 1  
