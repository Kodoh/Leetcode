class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        def char_occurrences(s: str) -> dict:
            occurrences = {}
            
            for char in s:
                if char in occurrences:
                    occurrences[char] += 1
                else:
                    occurrences[char] = 1
            
            return occurrences

        if len(word1) != len(word2):
            return False

        word1occ = char_occurrences(word1)
        word2occ = char_occurrences(word2)

        if set(word1occ.keys()) != set(word2occ.keys()):
            return False

        if sorted(word1occ.values()) != sorted(word2occ.values()):
            return False

        return True
