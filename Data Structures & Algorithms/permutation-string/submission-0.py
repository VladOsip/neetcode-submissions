class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
            
        count = [0] * 26
        for i in range(len(s1)):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
            
        if all(x == 0 for x in count):
            return True
            
        for i in range(len(s1), len(s2)):
            count[ord(s2[i]) - ord('a')] -= 1
            count[ord(s2[i - len(s1)]) - ord('a')] += 1
            
            if all(x == 0 for x in count):
                return True
                
        return False