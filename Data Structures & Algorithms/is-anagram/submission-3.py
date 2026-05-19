class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        countS, countT = [0] * 26, [0] * 26
            
        for i in range(len(s)):
            idxS = ord(s[i]) - ord('a')
            idxT = ord(t[i]) - ord('a')
            countS[idxS] += 1 
            countT[idxT] += 1 
                
        return countS == countT