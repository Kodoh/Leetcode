class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = set(s)
        res = 0
        odd = True
        for i in letters:
            if s.count(i) % 2 == 0:
                res += s.count(i)
            elif odd:
                res += s.count(i)
                odd = False
            else:
                res += s.count(i) - 1


        return res