class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s
            
        res = [[] for _ in range(numRows)]
        
        count = 0
        down = True
        for i in s:
            res[count].append(i)
            if down:
                count += 1
                if count >= numRows - 1:
                    down = False
            else:
                count -= 1
                if count == 0:
                    down = True
        
        return ''.join(''.join(row) for row in res)
                
