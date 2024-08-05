class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        sorted_array = sorted(points, key=lambda x: x[0])

        res = 1
        last = sorted_array.pop()[0]

        while sorted_array:
            new = sorted_array.pop()

            if last >= new[0] and last <= new[1]:
                pass
            else:
                last = new[0]
                res += 1

        return res
