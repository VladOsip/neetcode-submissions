class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
            
        count = Counter(hand)
        
        for num in sorted(count):
            if count[num] > 0:
                start_count = count[num]
                for i in range(groupSize):
                    if count[num + i] < start_count:
                        return False
                    count[num + i] -= start_count
                    
        return True