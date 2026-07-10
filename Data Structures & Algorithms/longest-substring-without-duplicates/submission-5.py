class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_set = set()
        max_len = 0
        left = 0

        for right in range(len(s)):
            while s[right] in check_set:
                check_set.remove(s[left])
                left+=1
            check_set.add(s[right])
            max_len = max(max_len, len(check_set))
        return max_len