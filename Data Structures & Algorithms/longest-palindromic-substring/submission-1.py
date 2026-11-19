class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        best = s[0]

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        for center in range(len(s)):
            odd = expand(center, center)
            even = expand(center, center + 1)
            if len(odd) > len(best):
                best = odd
            if len(even) > len(best):
                best = even

        return best