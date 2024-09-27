class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            middle = (l + r) // 2
            print(middle)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle  
            else:
                l = middle + 1

        return l  
