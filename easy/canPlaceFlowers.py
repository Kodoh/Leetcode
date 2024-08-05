class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) and n != 0:
            if flowerbed[max(0,i-1)] == 0 and flowerbed[i] == 0 and flowerbed[min(i+1,len(flowerbed)-1)] == 0:
                n -= 1
                i += 2
            else:
                i += 1

        return n == 0
