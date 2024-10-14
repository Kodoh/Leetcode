class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted([int(t[:2]) * 60 + int(t[3:]) for t in timePoints])
        res = 1440
        
        for i in range(1,len(minutes)):
            res = min(res,minutes[i]-minutes[i-1])
        
        res = min(res, 1440+minutes[0] - minutes[-1])
        return res
        

