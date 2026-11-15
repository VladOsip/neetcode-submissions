class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128
        left = 0
        result = 0

        for right in range(len(s)):
            char_code = ord(s[right])
            
            if last_seen[char_code] >= left:
                left = last_seen[char_code] + 1
            
            last_seen[char_code] = right
            result = max(result, right - left + 1)
            
        return result