class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
            
        events.sort(key=lambda x: (x[0], -x[1]))
        
        solution = []
        counter = 0
        start_i = None
        
        for coord, event_type in events:
            if counter == 0:
                start_i = coord  

            counter += event_type
            
            if counter == 0:
                solution.append([start_i, coord]) 
                
        return solution