from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)
        need = len(dict_t)
        
        window = {}
        have = 0
        
        res, res_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in dict_t and window[char] == dict_t[char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in dict_t and window[left_char] < dict_t[left_char]:
                    have -= 1
                
                left += 1
        
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""