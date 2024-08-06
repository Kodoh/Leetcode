class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def helper(l, u):
            if l == u:
                return l
            middle = (l + u) // 2
            
            if nums[middle] > nums[middle + 1]:
                return helper(l, middle)
            else:
                return helper(middle + 1, u)
        
        return helper(0, len(nums) - 1)
