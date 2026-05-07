class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Quick length check
        if len(s) != len(t):
            return False
        
        # Step 2: Use a dictionary to count frequencies
        countS, countT = {}, {}
        
        for i in range(len(s)):
            # get(char, 0) handles cases where the char isn't in the dict yet
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # Step 3: Compare the two hash maps
        return countS == countT