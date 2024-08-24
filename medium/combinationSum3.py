class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []

        def helper(sub, i, k, n):
            if len(sub) == k or i > 9:
                if len(sub) == k and sum(sub) == n:
                    self.res.append(sub[:])  
                return

            sub.append(i)
            helper(sub, i + 1, k, n)  
            
            sub.pop()
            helper(sub, i + 1, k, n)  

        helper([], 1, k, n)
        return self.res
