class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        MAX = 3
        products.sort()
        
        res = []

        # Helper function to perform binary search
        def binary_search(products, prefix):
            left, right = 0, len(products)
            while left < right:
                mid = (left + right) // 2
                if products[mid] < prefix:
                    left = mid + 1
                else:
                    right = mid
            return left

        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[:i]
            start_index = binary_search(products, prefix)
            current = []
            for j in range(start_index, len(products)):
                if products[j].startswith(prefix):
                    current.append(products[j])
                    if len(current) == MAX:
                        break
                else:
                    break
            res.append(current)
        
        return res
