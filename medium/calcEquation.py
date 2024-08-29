class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        res = []
        graph = {}
        for i in range(len(equations)):
            if equations[i][0] not in graph:
                graph[equations[i][0]] = {}
            if equations[i][1] not in graph:
                graph[equations[i][1]] = {}
            
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1/values[i]

        def dfs(graph, visited, start, finish, current):
            if start == finish:
                return current

            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    result = dfs(graph, visited, neighbor, finish, current * graph[start][neighbor])
                    if result != -1:  
                        return result

            visited.remove(start)  
            return -1 

        res = []
        for start, finish in queries:
            if start not in graph or finish not in graph:
                res.append(-1)  
            else:
                res.append(dfs(graph, set(), start, finish, 1))

        return res
