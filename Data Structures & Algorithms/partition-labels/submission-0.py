class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i
            
        res = []
        anchor = 0
        j = 0
        for i, c in enumerate(s):
            j = max(j, last[ord(c) - ord('a')])
            if i == j:
                res.append(i - anchor + 1)
                anchor = i + 1
                
        return res