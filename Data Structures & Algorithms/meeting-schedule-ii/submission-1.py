class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
            
        events.sort(key=lambda x: (x[0], x[1]))
        
        max_rooms = 0
        current_rooms = 0
        
        for coord, event_type in events:
            current_rooms += event_type
            max_rooms = max(max_rooms, current_rooms)
            
        return max_rooms