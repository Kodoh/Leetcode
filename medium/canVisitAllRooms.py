class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def dfs(visited,i):
            current = rooms[i]

            for j in current:
                if j not in visited:
                    visited.add(j)
                    dfs(visited,j)

        
        visited = {0}
        dfs(visited,0)

        
        return len(visited) == len(rooms)
