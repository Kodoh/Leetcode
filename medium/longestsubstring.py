class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1

        longest = 0
        while left <= len(s) and right <= len(s):
            if len(s[left:right]) == len(set(s[left:right])):
                longest = max(longest,len(s[left:right]))
                right += 1 
            else:
                left += 1
                if left > right:
                    right = left
        return longest