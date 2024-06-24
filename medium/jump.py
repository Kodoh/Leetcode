class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if not nums:
            return False
        
        furthest = nums[0]
        for i in range(1,len(nums)-1):
            if i <= furthest:
                furthest = max(furthest,i+nums[i])


            
        return len(nums) - 1 <= furthest