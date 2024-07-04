class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
    
        def recur(i, stack, n, k, res):
            if len(stack) == k:
                res.append(stack[:])
                return
            
            for j in range(i, n + 1):
                stack.append(j)
                recur(j + 1, stack, n, k, res)
                stack.pop()


        recur(1,[],n,k,res)       

        
        return res
