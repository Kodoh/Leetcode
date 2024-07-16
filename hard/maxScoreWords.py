class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        maxScore = 0
        letterScore = {}

        setLetters = set(letters)
        while setLetters:
            new = setLetters.pop()
            letterScore[new] = letters.count(new) * score[ord(new) - 97]


        def powerset(s):
            x = len(s)
            masks = [1 << i for i in range(x)]
            for i in range(1 << x):
                yield [ss for mask, ss in zip(masks, s) if i & mask]
        
        subsets = list(powerset(words))
        
        for i in subsets:
            current = 0
            compdict = letterScore.copy()
            single = ''.join(i)
            for j in single:
                if j in compdict:
                    if compdict[j] > 0:
                        compdict[j] -= score[ord(j) - 97]
                        current += score[ord(j) - 97]
                    else:
                        current = 0
                        break
                else:
                    current = 0
                    break
            maxScore = max(maxScore,current)


        return maxScore

