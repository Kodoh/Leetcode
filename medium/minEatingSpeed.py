class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def canFinishWithSpeed(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k  
            return hours <= h

        l, u = 1, max(piles)
        while l <= u:
            mid = (l + u) // 2
            if canFinishWithSpeed(mid):
                u = mid - 1  
            else:
                l = mid + 1  

        return l
