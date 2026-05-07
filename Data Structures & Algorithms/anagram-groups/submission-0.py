class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for s in strs:
            charMap = [0] * 26

            for character in s:
                charMap[ord(character)-ord('a')]+=1
            
            key = tuple(charMap)

            if key not in groups:
                groups[key] = []
            
            groups[key].append(s)
        
        return list(groups.values())
