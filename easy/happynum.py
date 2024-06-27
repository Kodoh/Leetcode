class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        seen = set()
        while int(n) != 1:
            if int(n) in seen:
                return False
            s = 0
            seen.add(int(n))
            for i in n:
                s += int(i)**2
            n = str(s)
        
        return True