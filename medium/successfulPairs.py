class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        res = [0] * len(spells)
        potions.sort()


        def find_smallest_greater_than(arr, x):
            
            index = bisect.bisect_left(arr, x)
            if index < len(arr):
                return index
            else:
                return None  


        for i in range(len(spells)):
            ind = find_smallest_greater_than(potions,success/spells[i])
            if ind:
                res[i] = len(potions) - ind 
            elif potions[0] * spells[i] >= success:
                res[i] = len(potions)


        return res
