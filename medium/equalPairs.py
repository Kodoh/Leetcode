class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        res = 0
        
        for i in grid:
            if tuple(i) in rows:
                rows[tuple(i)] += 1
            else:
                rows[tuple(i)] = 1

        def get_column(matrix, column_index):
            return [row[column_index] for row in matrix]

        for i in range(len(grid[0])):
            column = get_column(grid, i)
            if tuple(column) in rows:
                res += rows[tuple(column)]
        
        return res
