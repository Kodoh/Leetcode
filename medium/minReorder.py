class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.changes = 0
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, True))  
            graph[v].append((u, False)) 

        def dfs(current):
            for neighbor, direction in graph[current]:
                if neighbor not in visited:
                    if direction: 
                        self.changes += 1
                    visited.add(neighbor)  
                    dfs(neighbor)

        visited = set([0]) 
        dfs(0)
        return self.changes
