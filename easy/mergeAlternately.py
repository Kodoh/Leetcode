class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ''

        if len(word1) < len(word2):
            shortest = word1
            longest = word2

        else:
            shortest = word2
            longest = word1

        
        for i in range(len(shortest)):
            res += word1[i]
            res += word2[i]

        
        res += longest[i+1:len(longest)]

        return res
