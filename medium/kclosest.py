class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        hashmap = {}
        for i in range(len(points)):
            dist = math.sqrt(points[i][0]**2 + points[i][1]**2)
            hashmap[i] = dist 

        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1]))

        for i in hashmap:
            if len(res) == k:
                break
            else:
                res.append(points[i])

        return res