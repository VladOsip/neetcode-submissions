class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use 128 to cover all standard ASCII characters (not just 'a-z')
        last_seen = [-1] * 128 
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            char_code = ord(s[right])
            
            # If we've seen this char and it's within our current window
            if last_seen[char_code] >= left:
                # Jump 'left' to one position after the previous occurrence
                left = last_seen[char_code] + 1
            
            # Update the last seen index for this character
            last_seen[char_code] = right
            
            # Update the max length found so far
            # (right - left + 1) is the length of the current window
            max_len = max(max_len, right - left + 1)
            
        return max_len