class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current = max(candies)
        res = []
        for i in candies:
            res.append(i + extraCandies >= current)

        return res
