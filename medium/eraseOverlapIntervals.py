class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        sorted_array = sorted(intervals, key=lambda x: x[0])

        res = 0
        last = sorted_array.pop()[0]

        while sorted_array:
            new = sorted_array.pop()

            if last >= new[0] and last < new[1]:
                res += 1
            else:
                last = new[0]

        return res
