class Solution {
public:
    bool canAttendMeetings(std::vector<Interval>& intervals) {
        if (intervals.empty()) return true;
        
        std::sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) {
            return a.start < b.start;
        });
        
        for (size_t i = 1; i < intervals.size(); ++i) {
            if (intervals[i].start < intervals[i-1].end) {
                return false;
            }
        }
        
        return true;
    }
};