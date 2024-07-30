class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city_index):
            stack = [city_index]
            while stack:
                city = stack.pop()
                for neighbor in range(len(isConnected)):
                    if isConnected[city][neighbor] == 1 and neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        visited = set()
        res = 0
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
                
        return res
