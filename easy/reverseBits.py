class Solution:
    def reverseBits(self, n: int) -> int:
        a = str(bin(n)[2:])
        a = a.zfill(32)[::-1]
        return int(a,2)
