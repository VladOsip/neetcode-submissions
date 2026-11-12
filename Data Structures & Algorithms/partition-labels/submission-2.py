class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
        
        partitions = []
        start = 0
        end = 0
        
        for i, ch in enumerate(s):
            end = max(end, last[ord(ch) - ord('a')])
            
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
                
        return partitions