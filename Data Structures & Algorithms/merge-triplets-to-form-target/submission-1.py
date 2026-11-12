class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_0 = found_1 = found_2 = False
        t0, t1, t2 = target

        for a, b, c in triplets:
            if a > t0 or b > t1 or c > t2:
                continue
            
            if a == t0: found_0 = True
            if b == t1: found_1 = True
            if c == t2: found_2 = True
            
            if found_0 and found_1 and found_2:
                return True
                
        return found_0 and found_1 and found_2