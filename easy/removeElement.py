class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                temp = nums[-1]
                nums[-1] = nums[i]
                nums[i] = temp
                nums.pop()
            else:
                count += 1
            i -= 1
        return count