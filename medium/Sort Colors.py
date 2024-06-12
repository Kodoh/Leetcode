class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {0:0,1:0,2:0}

        for i in nums:
            hashmap[i] += 1
        

        current = 0  

        for key, value in hashmap.items():
            new = current + value
            nums[current:new] = [key] * value
            current = new  
        

# O(n) time / space         -> can be made better using Dutch flag algo