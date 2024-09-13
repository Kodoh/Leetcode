class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}

        def dfs(node):
            if node in visited:  
                return visited[node]
            
            new_node = Node(node.val)
            visited[node] = new_node 
            
            for neighbor in node.neighbors:
                new_node.neighbors.append(dfs(neighbor))  
            
            return new_node

        return dfs(node)
