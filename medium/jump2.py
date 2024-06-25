class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [0]
        for i in range(len(nums)-2, -1, -1):

            if nums[i] != 0:
                jumps.insert(0,min(jumps[0:min(nums[i],len(jumps))]) + 1)
            else:
                jumps.insert(0,float('inf'))
        
        return jumps[0]