class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minVal = nums[0]
        secondVal = max(nums)

        queue = deque(nums)  


        while queue:
            latest = queue.popleft()
            if latest > secondVal:
                return True
            elif latest <= minVal:
                minVal = latest 
            elif latest > minVal and latest < secondVal:
                secondVal = latest
            

        return False