class Solution:
    def countSubstrings(self, s: str) -> int:
        total_palindromes = 0

        def expand_and_count(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        for i in range(len(s)):
            total_palindromes += expand_and_count(i, i)
            total_palindromes += expand_and_count(i, i + 1)

        return total_palindromes