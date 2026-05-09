class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        max_freq = 0
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            counts[index] += 1
            
            max_freq = max(max_freq, counts[index])
            
            if (right - left + 1) - max_freq > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len