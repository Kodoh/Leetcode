class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        paired = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        min_heap = []
        max_score = 0
        current_sum = 0
        
        for num1, num2 in paired:
            heapq.heappush(min_heap, num1)
            current_sum += num1
            
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * num2)
        
        return max_score
