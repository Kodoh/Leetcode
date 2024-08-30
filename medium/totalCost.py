class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        leftInd = candidates
        first = costs[0:candidates]
        heapq.heapify(first)
        if len(costs)-candidates >= candidates:
            last = costs[len(costs)-candidates:len(costs)]
            rightInd = len(costs)-candidates - 1
        else:
            last = costs[candidates:]
            rightInd = candidates - 1
        heapq.heapify(last)

        
        for i in range(k):
            if len(first) == 0 and len(last) == 0:
                break
            
            if len(first) > 0:
                fpop = heapq.heappop(first)
            else:
                lpop = heapq.heappop(last)
                res += lpop
                continue
            if len(last) > 0:
                lpop = heapq.heappop(last)
            else:
                res += fpop
                continue

            if fpop <= lpop:
                res += fpop
                heapq.heappush(last, lpop)
                if leftInd <= rightInd:
                    heapq.heappush(first, costs[leftInd])
                    leftInd += 1 
            else:
                res += lpop
                heapq.heappush(first, fpop)
                if rightInd >= leftInd:
                    heapq.heappush(last, costs[rightInd])
                    rightInd -= 1 

        return res
