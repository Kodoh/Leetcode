class Solution:
    def pivotInteger(self, n: int) -> int:
        currentLeft = 0
        currentRight = sum(range(1, n+1))  
        for i in range(1, n+1):
            currentRight -= i  
            if currentLeft == currentRight:
                return i
            currentLeft += i 

        return -1
