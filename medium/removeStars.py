class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        strdel = 0

        for char in reversed(s):
            if char == '*':
                strdel += 1
            else:
                if strdel == 0:
                    res.append(char)
                else:
                    strdel -= 1

        return ''.join(reversed(res))
