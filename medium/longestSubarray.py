class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = []

        currentZero = 0
        amountZeros = 0
        res = 0

        left = 0
        right = 0

        if 1 not in nums:
            return 0

        while right < len(nums):
            if nums[right] == 1:
                res = max(res,right - left)
                right += 1 

            elif nums[right] == 0:
                amountZeros += 1 
                zeros.append(right)
                if amountZeros > 1:
                    amountZeros = 1
                    left = zeros[currentZero] + 1
                    currentZero += 1 
                else:
                    res = max(res,right - left)
                right += 1 
            
        return res
