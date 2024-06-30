class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        df = [0] * (len(cost) - 2)
        df.append(cost[-2])
        df.append(cost[-1])


        i = len(cost) - 3
        while i >= 0:
            df[i] = cost[i] + min(df[i+1],df[i+2])
            i -=1

        return min(df[0],df[1])