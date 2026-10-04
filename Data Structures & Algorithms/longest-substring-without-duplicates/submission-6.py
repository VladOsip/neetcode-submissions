class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        locate = {}  

        for end, char in enumerate(s):
            if char in locate:
                start = max(start, locate[char] + 1)
            
            locate[char] = end
            max_len = max(max_len, end - start + 1)

        return max_len