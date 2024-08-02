class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        largest = len(bin(max(a,b,c))[2:])
        a = str(bin(a))[2:].zfill(largest)
        b = str(bin(b))[2:].zfill(largest)
        c = str(bin(c))[2:].zfill(largest)
        
        count = 0
        for i in range(len(a)):
            if c[i] == '0' and (int(a[i]) & int(b[i])):
                count += 2
            
            elif c[i] == '0' and (int(a[i]) | int(b[i])):
                count += 1
            
            elif c[i] == '1' and not (int(a[i]) | int(b[i])):
                count += 1

        return count
