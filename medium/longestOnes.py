class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = []

        currentZero = 0
        amountZeros = 0
        res = 0

        left = 0
        right = 0


        while right < len(nums):
            if nums[right] == 1:
                res = max(res,right - left + 1)
                right += 1 

            elif nums[right] == 0:
                amountZeros += 1 
                zeros.append(right)
                if amountZeros > k:
                    amountZeros = k
                    left = zeros[currentZero] + 1
                    currentZero += 1 
                else:
                    res = max(res,right - left + 1)
                right += 1 
            
        return (res)
