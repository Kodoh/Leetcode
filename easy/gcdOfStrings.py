class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallest = min(str1, str2)
        largest = max(str1, str2)
        
        end = len(smallest)


        while end > 0:
            if smallest[:end] * (len(largest)// len(smallest[:end])) == largest and smallest[:end] * (len(smallest)// len(smallest[:end])) == smallest:
                return smallest[:end]
            end -= 1

        return ''
