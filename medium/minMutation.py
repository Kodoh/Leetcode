class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def diff_isone(s1,s2):
            count = 0
            for i in range(8):
                if s1[i] != s2[i]:
                    count += 1
                    if count > 1:
                        return False
                    else:
                        count += 1 
            
            return True
        
        queue = deque()
        queue.append((startGene,0))
        visited = set()


        while queue:
            current, counter = queue.popleft()
            if current == endGene:
                return counter
            
            for gene in bank:
                if (gene not in visited) and (diff_isone(current,gene)):
                    visited.add(gene)
                    queue.append((gene,counter+1))
            

        return -1
