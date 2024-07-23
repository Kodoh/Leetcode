class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        res = []
        hashmap = {}
        for i in set(nums):
            count = nums.count(i)
            if count in hashmap:
                hashmap[count].extend([i]*count)
            else:
                hashmap[count] = [i]*count

        
        sorted_hashmap = dict(sorted(hashmap.items()))

        for i in sorted_hashmap:
            arr = sorted(sorted_hashmap[i], reverse=True)
            res.extend(arr)

        return res
