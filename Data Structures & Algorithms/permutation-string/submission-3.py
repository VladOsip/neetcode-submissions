class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False
            
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # Count how many starting letters match perfectly
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # Slide the window
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            # Character entering the window on the right
            r_idx = ord(s2[i]) - ord('a')
            s2_count[r_idx] += 1
            if s1_count[r_idx] == s2_count[r_idx]:
                matches += 1
            elif s1_count[r_idx] + 1 == s2_count[r_idx]:
                matches -= 1
                
            # Character leaving the window on the left
            l_idx = ord(s2[i - len(s1)]) - ord('a')
            s2_count[l_idx] -= 1
            if s1_count[l_idx] == s2_count[l_idx]:
                matches += 1
            elif s1_count[l_idx] - 1 == s2_count[l_idx]:
                matches -= 1
                
        return matches == 26