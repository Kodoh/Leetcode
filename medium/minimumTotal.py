class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        dp = []
        def dfs(current,level):
            if level > 0:
                temp = []

                for i in range(len(current)):
                    temp.append(current[i] + min(dp[-1][max(i-1,0)],dp[-1][min(i,len(dp[-1])-1)]))
                dp.append(temp)

            else:
                dp.append(current)
            
            level += 1
            if level == len(triangle):
                return

            dfs(triangle[level],level)
            
        dfs(triangle[0],0)

        return min(dp[-1])
        
